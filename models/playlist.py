from models.base_media import BaseMedia


class Playlist(BaseMedia):
    def __init__(self, title, url, count, thumbnail):
        super().__init__(title, url, thumbnail)
        self.count = count
