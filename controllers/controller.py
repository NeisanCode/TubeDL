from services import YouTubeService
from services import Engine
from controllers.decorators import handle_error


class Controller:
    @staticmethod
    @handle_error
    def analyse_url(url):
        yt_service = YouTubeService()
        return yt_service.analyze_url(url)

    @staticmethod
    @handle_error
    def download(media, queue):
        downloader = Engine(media, queue)
        downloader.download_media()
