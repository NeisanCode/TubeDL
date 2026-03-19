from PIL import Image
from customtkinter import CTkImage


class Icons:
    logo = "assets/icons/logo.ico"
    cookie = "assets/icons/cookie.png"
    download = "assets/icons/download.png"
    ffmpeg = "assets/icons/ffmpeg.png"
    folder = "assets/icons/folder.png"
    play_btn = "assets/icons/play-btn.png"

    @staticmethod
    def load_img(img):
        image = Image.open(img).convert("RGBA")
        size = (32, 32)
        image = image.resize(size)
        ctk_image = CTkImage(light_image=image, dark_image=image, size=size)
        return ctk_image
