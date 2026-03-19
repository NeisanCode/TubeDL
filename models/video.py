from models.base_media import BaseMedia


class Video(BaseMedia):
    def __init__(self,id,  title, url, thumbnail, res_list=None):
        super().__init__(id, title, url, thumbnail)
        self.resols = res_list or []
        self.download_resol = None
