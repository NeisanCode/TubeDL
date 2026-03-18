from models.base_media import BaseMedia


class Short(BaseMedia):
    def __init__(self, title, url, thumbnail):
        super().__init__(title, url, thumbnail)
        self.is_vertical = True
