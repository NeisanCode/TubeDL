import re
import os
from queue import Queue
from pprint import pprint
import yt_dlp
from core.config import Config
from models.playlist import Playlist
from models.short import Short
from models.video import Video
from services.helpers import get_format_selector


def _strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


class Downloader:
    def __init__(self, media: Video | Short | Playlist, queue: Queue):
        self.media = media
        self.queue = queue
        self.ydl_opts = {
            "quiet": False,  # ← temporairement
            "no_warnings": True,  # ← temporairement
            "ignoreerrors": True,  # ← temporairement
            "progress_hooks": [self._progress_hook],
            "postprocessor_hooks": [self._postprocessor_hook],  # ← ajoute ça
            "cookiefile": "cookies/cookies.txt",  # ← commente ça
            "merge_output_format": "mp4",
            "format_sort": ["res", "codec:h264"],
            "no_overwrites": True,  # ← confirme le comportement skip
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
        output_dir = Config.download_path
        video_opts = {
            **self.ydl_opts,
            "format": get_format_selector(self.media.resol_selected),
            "outtmpl": os.path.join(output_dir, "Videos/%(title)s.%(ext)s"),
        }
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([url])

    def _download_short(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def _download_playlist(self, url):
        output_dir = Config.download_path
        playlist_opts = {
            **self.ydl_opts,
            "outtmpl": os.path.join(
                output_dir, "%(playlist_index)s - %(title)s.%(ext)s"
            ),
            "noplaylist": False,
        }
        with yt_dlp.YoutubeDL(playlist_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            playlist_title = info.get("title", "Playlist inconnue")
            total = len(info.get("entries", []))
            print(f"\n🎬 Playlist : {playlist_title}")
            print(f"📦 {total} vidéo(s) à télécharger\n")
            ydl.download([url])

    def _progress_hook(self, d: dict):
        if d["status"] == "downloading":
            if self.queue:
                downloaded = d.get("downloaded_bytes", 0)
                total = d.get("total_bytes") or d.get("total_bytes_estimate", 0)
                percent = (downloaded / total) if total else 0
                self.queue.put(
                    {
                        "percent": percent,
                        "speed": _strip_ansi(d.get("_speed_str", "—")).strip(),
                    }
                )
            else:
                title = d["info_dict"].get("title", "Inconnu")
                percent = d.get("_percent_str", "?%").strip()
                speed = d.get("_speed_str", "?").strip()
                print(
                    f"\r  ⬇ [{title}] {percent}  vitesse: {speed}", end="", flush=True
                )

    def _postprocessor_hook(self, d: dict):
        if d["status"] == "finished":
            if self.queue:
                self.queue.put({"percent": 1.0, "speed": "✔ Terminé"})
            elif self.queue.empty():
                self.queue.put(
                    {
                        "percent": 1.0,
                        "speed": "✔ Terminé",
                        "status": "downloaded",
                    }
                )
