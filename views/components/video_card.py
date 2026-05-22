from .basecard import _BaseCard
from views.themes.color import *
import customtkinter as ctk
from PIL import Image
from utils import round_corners

class VideoCard(_BaseCard):
    def __init__(self, parent, title: str, quality: str = "720P", duration: str = "0:00", queue=None, preview_image=round_corners(Image.open("assets/images/fallback.png")), on_download=None, **kwargs):
        self.quality = quality
        self.duration = duration
        super().__init__(
            parent, title=title, queue=queue, on_download=on_download,
            tag_text="Vidéo", tag_color=TAG_VIDEO, tag_fg=TAG_VIDEO_TEXT,
            preview_image=preview_image, **kwargs
        )

    def _build_meta(self, tag_text, tag_color, tag_fg):
        ctk.CTkLabel(
            self.thumb, text=f" {self.duration} ",
            font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color=TEXT_LIGHT, fg_color="#1A1A1A", height=16, corner_radius=4
        ).place(relx=0.92, rely=0.92, anchor="se")

        ctk.CTkLabel(self.meta, text=self.quality, font=ctk.CTkFont(family="Segoe UI", size=13), text_color=TEXT_GRAY).pack(side="left", padx=(0, 12))

        ctk.CTkLabel(
            self.meta, text=tag_text.upper(), font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            fg_color=tag_color, text_color=tag_fg, height=22, corner_radius=6, padx=8
        ).pack(side="left")