from models.media import Media


class Short(Media):
    def __init__(self, title, url, duration):
        super().__init__(title, url, duration)
        self.is_vertical = True
