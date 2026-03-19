from customtkinter import CTkImage
from PIL import Image, ImageDraw
import requests
from io import BytesIO


def converto_img(url, radius=10):
    response = requests.get(url)
    img_data = response.content
    image = Image.open(BytesIO(img_data)).convert("RGBA")
    size = (369, 207)
    image = image.resize(size)
    # 🔵 Création du masque arrondi
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=255)
    # 🔵 Appliquer le masque (alpha)
    image.putalpha(mask)
    # 🔵 Conversion en CTkImage
    ctk_image = CTkImage(light_image=image, dark_image=image, size=size)
    return ctk_image


def resize_img():
    pass
