from services import YouTubeService
from pprint import pprint
video_url = "https://youtu.be/1AF5pFGwRTM?si=GpFTMmynJinTYaG3"
yt_service = YouTubeService()
media = yt_service.analyze_url(video_url)
pprint(media.__dict__, indent=2)