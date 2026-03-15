import yt_dlp
from models import Video, Short, Playlist


class YouTubeService:
    def __init__(self):
        self.ydl_opts = {
            "extract_flat": True,
            "quiet": True,
        }

    def analyze_url(self, url):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if info.get("_type") == "playlist":
                return Playlist(
                    title=info.get("title"),
                    url=url,
                    count=len(info.get("entries", [])),
                )

            is_short = "/shorts/" in url or (info.get("duration", 0) <= 60)

            if is_short:
                return Short(
                    title=info.get("title"),
                    url=url,
                )

            return Video(
                title=info.get("title"),
                url=url,
                res_list=self._extract_resolutions(info),
            )

    def _extract_resolutions(self, info):
        resolutions = set(
            f"{f['height']}p"
            for f in info["formats"]
            if f.get("height") and f.get("vcodec") != "none"
        )
        return sorted(resolutions, key=lambda x: int(x[:-1]), reverse=True)
