from models.video import Video


class Short(Video):
    def __init__(self, id, title, url, thumbnail, duration, res_list=[]):
        super().__init__(id, title, url, thumbnail, duration, res_list)
        self.is_vertical = True
