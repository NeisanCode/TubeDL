from models.base_media import BaseMedia


class Video(BaseMedia):
    def __init__(self, title, url, thumbnail, res_list=None):
        super().__init__(title, url, thumbnail)
        self.resols = res_list or []

