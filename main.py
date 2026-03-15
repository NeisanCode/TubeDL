from pprint import pprint
from service.downloader import Downloader
from service.youtube_service import YouTubeService

from view import App


if __name__ == "__main__":
    app = App()
    app.mainloop()

# url = "https://youtu.be/iV-x42CU8PU"
# yt_service = YouTubeService()
# media = yt_service.analyze_url(url)