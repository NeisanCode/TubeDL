from models.video import Video


class Short(Video):
    def __init__(self, id, title, url, thumbnail, res_list=None):
        super().__init__(id, title, url, thumbnail, res_list)
        self.is_vertical = True
