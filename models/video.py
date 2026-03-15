from models.base_media import BaseMedia


class Video(BaseMedia):
    def __init__(self, title, url, res_list=None):
        super().__init__(title, url)
        self.resols = res_list or []
