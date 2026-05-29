import re
import os
from queue import Queue
import shutil
import yt_dlp
from core import AppSettings, AppConfig
from models.playlist import Playlist
from models.short import Short
from models.video import Video
from .helpers import get_format_selector, load_cookie


def _strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


class Engine:
    def __init__(self, media: Video | Short | Playlist, queue: Queue):
        self.media = media
        self.queue = queue
        self.ydl_opts = {
            "format": "bestvideo[ext=mp4][vcodec^=avc1]+bestaudio[ext=m4a]/bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "ffmpeg_location": AppConfig.FFMPEG_BINARY_DIR,
            "quiet": False,
            "ignoreerrors": False,
            "progress_hooks": [self._progress_hook],
            "postprocessor_hooks": [self._postprocessor_hook],
            **load_cookie(),
        }

    def download_media(self):
        match self.media:
            case Video():
                self._download_video(self.media.url)
            case Short():
                self._download_short(self.media.url)
            case Playlist():
                self._download_playlist(self.media.url)

    def _download_video(self, url):
        output_dir = AppSettings.load_download_folder()
        format_selector = get_format_selector(self.media.resol_selected)
        video_opts = {
            **self.ydl_opts,
            "format": format_selector,
            "outtmpl": os.path.join(output_dir, "Videos/%(title)s.%(ext)s"),
        }

        print(f"📥 Téléchargement vidéo avec le format : {format_selector}")
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([url])

    def _download_short(self, url):
        output_dir = AppSettings.load_download_folder()
        short_opts = {
            **self.ydl_opts,
            "outtmpl": os.path.join(output_dir, "Shorts/%(title)s.%(ext)s"),
        }
        with yt_dlp.YoutubeDL(short_opts) as ydl:
            ydl.download([url])

    def _download_playlist(self, url):
        output_dir = AppSettings.load_download_folder()

        # 1. On extrait d'abord les infos de la playlist TRÈS RAPIDEMENT avec extract_flat
        flat_opts = {**self.ydl_opts, "extract_flat": True, "quiet": True}
        with yt_dlp.YoutubeDL(flat_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            playlist_title = info.get("title", "Playlist inconnue")
            total = len(info.get("entries", []))
            print(f"\n🎬 Playlist : {playlist_title}")
            print(f"📦 {total} vidéo(s) détectée(s)\n")

        # 2. On lance le téléchargement réel sans extract_flat
        playlist_opts = {
            **self.ydl_opts,
            "outtmpl": os.path.join(
                output_dir,
                "Playlists/%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s",
            ),
            "noplaylist": False,
        }
        with yt_dlp.YoutubeDL(playlist_opts) as ydl:
            ydl.download([url])

    def _progress_hook(self, d: dict):
        if d["status"] == "downloading":
            info = d.get("info_dict", {})
            current_video = info.get("playlist_index", 1)

            if self.queue:
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
                percent = (downloaded / total) if total else 0
                self.queue.put(
                    {
                        "percent": percent,
                        "speed": _strip_ansi(d.get("_speed_str", "—")).strip(),
                        "current_video": current_video,
                    }
                )
            else:
                title = info.get("title", "Inconnu")
                percent = d.get("_percent_str", "?%").strip()
                speed = d.get("_speed_str", "?").strip()
                print(
                    f"\r  ⬇ [{title}] {percent}  vitesse: {speed}", end="", flush=True
                )

    def _postprocessor_hook(self, d: dict):
        if d["status"] == "finished":
            if self.queue:
                info = d.get("info_dict", {})
                current_video = info.get("playlist_index", 1)
                self.queue.put(
                    {
                        "percent": 1.0,
                        "speed": "✔ Terminé",
                        "current_video": current_video,
                    }
                )
