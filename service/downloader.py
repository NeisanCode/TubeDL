from core.config import Config
import yt_dlp
import os
from models.playlist import Playlist
from models.short import Short
from models.video import Video


class Downloader:
    def __init__(self, media: Video | Short | Playlist):
        self.media = media
        self.ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "quiet": True,
            "no_warnings": True,
            "ignoreerrors": True,
            "progress_hooks": [self._progress_hook],
            "cookiesfrombrowser": (Config.browser_name, None, None, None),
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
        OUTPUT_DIR = Config.download_path
        VIDEO_DIR = "Videos/%(title)s.%(ext)s"

        self.ydl_opts["outtmpl"] = os.path.join(OUTPUT_DIR, VIDEO_DIR)
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def _download_short(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])

    def _download_playlist(self, url):
        OUTPUT_DIR = Config.download_path
        PLAYLIST_DIR = "%(playlist_index)s - %(title)s.%(ext)s"

        self.ydl_opts["outtmpl"] = os.path.join(OUTPUT_DIR, PLAYLIST_DIR)
        self.ydl_opts["noplaylist"] = False

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
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
