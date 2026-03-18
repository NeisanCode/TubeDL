from customtkinter import CTkImage
from PIL import Image
import requests
from io import BytesIO


def converto_img(url):
    response = requests.get(url)
    img_data = response.content
    image = Image.open(BytesIO(img_data))
    size = (600, 150)
    image = image.resize(size)
    ctk_image = CTkImage(light_image=image, dark_image=image, size=size)
    return ctk_image
