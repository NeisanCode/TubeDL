import yt_dlp
from models import Video, Short, Playlist


class YouTubeService:
    def __init__(self):
        self.ydl_opts = {
            "extract_flat": True,
            "quiet": True,
            "skip_download": True,
        }

    def analyze_url(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if info.get("_type") == "playlist":
                thumbnail = self._get_playlist_thumbails(url)
                return Playlist(
                    title=info.get("title"),
                    url=url,
                    thumbnail=thumbnail,
                    count=len(info.get("entries", [])),
                )

            is_short = "/shorts/" in url or (info.get("duration", 0) <= 60)

            if is_short:
                return Short(
                    title=info.get("title"),
                    url=url,
                )
            thumbnail = self._get_video_thumbails(url)
            return Video(
                title=info.get("title"),
                url=url,
                thumbnail=thumbnail,
                res_list=self._extract_resolutions(info),
            )

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
        return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)
