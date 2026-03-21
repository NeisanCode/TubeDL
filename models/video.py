from models.base_media import BaseMedia


class Video(BaseMedia):
    def __init__(self, id, title, url, thumbnail, duration, res_list=[]):
        super().__init__(id, title, url, thumbnail)
        self.res_list = res_list
        self.resol_selected = None
        self.duration = duration
