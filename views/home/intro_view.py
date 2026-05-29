import customtkinter as ctk
from views.themes.color import *


class IntroView(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color=BG_WHITE)
        self._build()

    def _build():
        pass
