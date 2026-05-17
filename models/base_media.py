from PIL import Image
import requests
from io import BytesIO


class BaseMedia:
    def __init__(self, id, title, url, thumbnail):
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail = thumbnail
        self.pil_thumbnail = self.load_thumbnail()

    def load_thumbnail(self):
        try:
            response = requests.get(self.thumbnail, timeout=5)
            response.raise_for_status()

            img = Image.open(BytesIO(response.content))
            img.verify()  # vérifie que c'est bien une image

            # Re-open after verify (PIL trick)
            return Image.open(BytesIO(response.content)).convert("RGB")

        except Exception as e:
            return Image.open("assets/image/fallback.png").convert("RGB")
