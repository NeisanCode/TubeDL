import customtkinter as ctk
from views.themes.color import *


class SectionTitle(ctk.CTkLabel):
    """Reusable section break text."""

    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent,
            text=text,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=PRIMARY_ACCENT,
            anchor="w",
            **kwargs,
        )




