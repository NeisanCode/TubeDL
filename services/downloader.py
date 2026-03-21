from pprint import pprint
from core.config import Config
import yt_dlp
import os
from models.playlist import Playlist
from models.short import Short
from models.video import Video
from services.helpers import get_format_selector


class Downloader:
    def __init__(self, media: Video | Short | Playlist):
        self.media = media
        self.ydl_opts = {
            "quiet": True,
            "no_warnings": True,
            "ignoreerrors": True,
            "progress_hooks": [self._progress_hook],
            # "cookiesfrombrowser": ("chrome",),
            "cookiefile": "cookies/cookies.txt",
            "merge_output_format": "mp4",
            "format_sort": ["res", "codec:h264"],
        }

    def download_media(self):
        # pprint(self.media.__dict__)
        match self.media:
            case Video():
                self._download_video(self.media.url)
            case Short():
                self._download_short(self.media.url)
            case Playlist():
                self._download_playlist(self.media.url)

    def _download_video(self, url):
        output_dir = Config.download_path
        video_dir = "Videos/%(title)s.%(ext)s"

        video_opts = {
            **self.ydl_opts,
            "format": get_format_selector(self.media.resol_selected),
            "outtmpl": os.path.join(output_dir, video_dir),
        }
        with yt_dlp.YoutubeDL(video_opts) as ydl:
            ydl.download([url])

    def _download_short(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def _download_playlist(self, url):
        output_dir = Config.download_path
        video_dir = "%(playlist_index)s - %(title)s.%(ext)s"

        playlist_opts = {
            **self.ydl_opts,
            "outtmpl": os.path.join(output_dir, video_dir),
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
            title = d["info_dict"].get("title", "Inconnu")
            percent = d.get("_percent_str", "?%").strip()
            speed = d.get("_speed_str", "?").strip()
            print(f"\r  ⬇ [{title}] {percent}  vitesse: {speed}", end="", flush=True)

        elif d["status"] == "finished":
            print(f"\n  ✔ Terminé : {d['filename']}")
