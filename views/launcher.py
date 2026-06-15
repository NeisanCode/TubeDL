import customtkinter as ctk
from core import AppConfig, AppSettings
from views.themes.color import BG_WINDOW

ctk.set_appearance_mode(AppSettings.load_default_theme())


class Launcher(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"{AppConfig.APP_NAME} Launcher")
        self.attributes("-zoomed", True)
        self.configure(fg_color=BG_WINDOW)
        self.minsize(900, 600)
        MID_SIZE = "1100x700"
        self._build()

        def on_minimize(event):
            if self.state() == "iconic":
                self.after(100, lambda: self.geometry(MID_SIZE))

        self.bind("<Unmap>", on_minimize)

    def _build(self):
        pass
