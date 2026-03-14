from models.media import Media


class Video(Media):
    def __init__(self, title, url, duration, resolution_list=None):
        super().__init__(title, url, duration)
        self.resolutions = resolution_list or []
