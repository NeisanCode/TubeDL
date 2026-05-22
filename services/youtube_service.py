import yt_dlp
from models import Video, Short, Playlist
from services.helpers import clean_url, format_duration


class YouTubeService:
    def __init__(self):
        self.ydl_opts = {
            "extract_flat": True,
            "quiet": True,
            "skip_download": True,
            "noplaylist": True,
        }

    def analyze_url(self, url):
        url = clean_url(url)
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            media_id = info.get("id")
            duration = info.get("duration", 0)

            if info.get("_type") == "playlist":
                thumbnail = self._get_playlist_thumbails(url)
                return Playlist(
                    id=media_id,
                    title=info.get("title"),
                    url=url,
                    thumbnail=thumbnail,
                    count=info.get("playlist_count") or len(info.get("entries", [])),
                )

            thumbnail = self._build_thumbnail(media_id)
            is_short = "/shorts/" in url or (duration <= 60)
            formatted_duration = format_duration(duration)
            if is_short:
                print("detected short")
                return Short(
                    id=media_id,
                    title=info.get("title"),
                    url=url,
                    thumbnail=thumbnail,
                    duration=formatted_duration,
                )

            return Video(
                id=media_id,
                title=info.get("title"),
                url=url,
                thumbnail=thumbnail,
                duration=formatted_duration,
                res_list=self._extract_resolutions(info),
            )

    def _build_thumbnail(self, video_id: str) -> str:
        return f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"

    def _get_video_thumbails(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            thumbnail = info.get("thumbnail")
            return thumbnail

    def _get_playlist_thumbails(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            first_video = info["entries"][0]
            video_url = first_video["url"]

        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            thumbnail = video_info["thumbnail"]
        return thumbnail

    def _extract_resolutions(self, info):
        resolutions = set(
            f"{f['height']}p"
            for f in info["formats"]
            if f.get("height") and f.get("vcodec") != "none"
        )
        return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)[:4]
