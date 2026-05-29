from pprint import pprint
import yt_dlp
from .helpers import load_cookie, format_duration
from models import Video, Short, Playlist
from services.helpers import clean_url


class YouTubeService:
    def __init__(self):
        # On garde une configuration de base légère, mais SANS extract_flat par défaut
        self.ydl_opts = {
            "quiet": True,
            "skip_download": True,
            "noplaylist": True,
        }

    def analyze_url(self, url):
        url = clean_url(url)

        # Configuration d'analyse blindée pour la vidéo UNIQUE
        opts_analyse = {
            "quiet": True,
            "skip_download": True,
            "noplaylist": True,
            "extract_flat": False,
            **load_cookie(),
        }
        with yt_dlp.YoutubeDL(opts_analyse) as ydl:
            info = ydl.extract_info(url, download=False)

            media_id = info.get("id")
            duration = info.get("duration", 0)
            thumbnail = self._build_thumbnail(media_id)
            formatted_duration = format_duration(duration)

            # S'il s'agit d'un Short
            is_short = "/shorts/" in url or (duration <= 60)
            if is_short:
                return Short(
                    id=media_id,
                    title=info.get("title"),
                    url=url,
                    thumbnail=thumbnail,
                    duration=formatted_duration,
                )

            # C'est une vidéo classique, isolée avec succès de sa playlist !
            return Video(
                id=media_id,
                title=info.get("title"),
                url=url,
                thumbnail=thumbnail,
                duration=formatted_duration,
                res_list=self._extract_resolutions(
                    info
                ),  # Tu auras enfin toutes les résolutions dispo !
            )

    def _build_thumbnail(self, video_id: str) -> str:
        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    def _get_video_thumbails(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info.get("thumbnail")

    def _get_playlist_thumbails(self, url):
        # On utilise extract_flat ici pour récupérer le premier lien rapidement
        opts = {**self.ydl_opts, "extract_flat": True}
        with yt_dlp.YoutubeDL(opts) as ydl:
            info = ydl.extract_info(url, download=False)
            first_video = info["entries"][0]
            video_url = first_video["url"]

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            return video_info.get("thumbnail")

    def _extract_resolutions(self, info):
        resolutions = set()
        for f in info.get("formats", []):
            height = f.get("height")
            vcodec = f.get("vcodec")
            format_id = f.get("format_id", "")

            # Exclure storyboards (sb0, sb1...) et formats sans vidéo
            if not height:
                continue
            if vcodec == "none" or not vcodec:
                continue
            if format_id.startswith("sb"):
                continue

            resolutions.add(f"{height}p")

        return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)[:4]
