from models.base_media import BaseMedia


class Playlist(BaseMedia):
    def __init__(self, id, title, url, count, thumbnail):
        super().__init__(id, title, url, thumbnail)
        self.count = count
