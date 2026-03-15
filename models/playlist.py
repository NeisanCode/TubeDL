from models.base_media import BaseMedia


class Playlist(BaseMedia):
    def __init__(self, title, url, count):
        super().__init__(title, url)
        self.count = count
