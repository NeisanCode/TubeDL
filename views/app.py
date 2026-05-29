import customtkinter as ctk
from views.themes.color import *
from core import AppConfig, AppSettings
from .widgets.sidebar import Sidebar
from .home.home_view import HomeView
from .settings.settings_view import SettingsView

ctk.set_appearance_mode(AppSettings.load_default_theme())


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(AppConfig.APP_NAME)
        self.attributes("-zoomed", True)
        self.configure(fg_color=BG_WINDOW)
        self.minsize(900, 600)
        MID_SIZE = "1100x700"

        def on_minimize(event):
            if self.state() == "iconic":
                self.after(100, lambda: self.geometry(MID_SIZE))

        self.bind("<Unmap>", on_minimize)

        # ── SIDEBAR (Composant) ───────────────────────────────────────────────
        self.sidebar = Sidebar(self, on_change_tab=self.handle_tab_change)
        self.sidebar.pack(side="left", fill="y")

        # ── CONTENEUR PRINCIPAL ────────────────────────────────────────────────
        self.view_container = ctk.CTkFrame(self, fg_color="transparent")
        self.view_container.pack(side="left", fill="both", expand=True)

        # ── PAGES ─────────────────────────────────────────────────────────────
        self.home_view = HomeView(self.view_container)
        self.settings_view = SettingsView(self.view_container)

        # Page par défaut
        self.home_view.pack(fill="both", expand=True)

    def handle_tab_change(self, tab_id: str):
        if tab_id == "settings":
            self.home_view.pack_forget()
            self.settings_view.pack(fill="both", expand=True)
        else:
            self.settings_view.pack_forget()
            self.home_view.pack(fill="both", expand=True)

