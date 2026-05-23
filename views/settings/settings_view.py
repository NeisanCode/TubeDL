import customtkinter as ctk
from views.themes.color import *
from core.config import Config
from .widgets import SectionTitle, PathSelectorCard, CookiesCard, ThemeSelectorCard

class SettingsView(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._build()

    def _build(self):
        # ── Title Page ──
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", padx=32, pady=(32, 20))

        ctk.CTkLabel(
            title_frame, text="Paramètres", text_color=TEXT_DARK,
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold")
        ).pack(side="left")

        # ── Scrollable Container ──
        container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=32, pady=10)

        # 1. Downloads Setup
        SectionTitle(container, "Emplacements de téléchargement").pack(anchor="w", pady=(20, 10))
        
        default_dl = getattr(Config, "download_path", "~/Downloads")
        self.video_card = PathSelectorCard(container, "Dossier des Vidéos", default_dl)
        self.video_card.pack(fill="x", pady=6)
        
        self.playlist_card = PathSelectorCard(container, "Dossier des Playlists", default_dl)
        self.playlist_card.pack(fill="x", pady=6)

        # 2. Cookies Setup
        SectionTitle(container, "Cookies").pack(anchor="w", pady=(20, 10))
        self.cookies_card = CookiesCard(container)
        self.cookies_card.pack(fill="x", pady=6)

        # 3. Appearance Setup
        SectionTitle(container, "Apparence").pack(anchor="w", pady=(20, 10))
        self.theme_card = ThemeSelectorCard(container)
        self.theme_card.pack(fill="x", pady=6)