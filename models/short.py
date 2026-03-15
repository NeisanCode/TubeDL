from models.base_media import BaseMedia


class Short(BaseMedia):
    def __init__(self, title, url):
        super().__init__(title, url)
        self.is_vertical = True
