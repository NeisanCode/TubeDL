from PIL import Image
import customtkinter as ctk
def make_placeholder_image(width: int, height: int, color: str = "#2a3a5c"):
    img = Image.new("RGB", (width, height), color)
    return ctk.CTkImage(light_image=img, dark_image=img, size=(width, height))

