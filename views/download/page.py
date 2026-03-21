import customtkinter as ctk
from .components import TabBar, PlaylistsSection, VideosSection

class DownloadsPage(ctk.CTkFrame):
    """
    Page principale "Vos téléchargements".
    Colonne unique pleine largeur : titre + onglets + liste vidéos/playlists.
    """

    def __init__(self, parent, colors: dict, **kwargs):
        super().__init__(parent, fg_color=colors["bg_primary"], **kwargs)
        self.colors = colors
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self._build()

    # ── Construction ────────────────────────────
    def _build(self):
        self._build_left_column()

    def _build_left_column(self):
        left = ctk.CTkFrame(self, fg_color="transparent")
        left.grid(row=0, column=0, sticky="nsew", padx=24, pady=24)
        left.grid_rowconfigure(2, weight=1)
        left.grid_columnconfigure(0, weight=1)

        # Titre
        title = ctk.CTkLabel(
            left,
            text="Vos téléchargements",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors["text_primary"],
            anchor="w",
        )
        title.grid(row=0, column=0, sticky="w", pady=(0, 16))

        # Onglets
        self._tabs = TabBar(left, self.colors, on_change=self._on_tab_change)
        self._tabs.grid(row=1, column=0, sticky="w", pady=(0, 20))

        # Zone de contenu scrollable
        scroll = ctk.CTkScrollableFrame(
            left,
            fg_color="transparent",
            scrollbar_button_color=self.colors["border"],
            scrollbar_button_hover_color=self.colors["accent_primary"],
        )
        scroll.grid(row=2, column=0, sticky="nsew")
        scroll.grid_columnconfigure(0, weight=1)
        self._content_scroll = scroll

        # Sections (visibles par défaut: vidéos)
        self._section_videos = ctk.CTkFrame(scroll, fg_color="transparent")
        self._section_videos.pack(fill="x")

        videos_lbl = ctk.CTkLabel(
            self._section_videos,
            text="",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=self.colors["text_primary"],
            anchor="w",
        )
        videos_lbl.pack(fill="x")

        VideosSection(self._section_videos, self.colors).pack(fill="x", pady=(8, 0))

        self._section_playlists = ctk.CTkFrame(scroll, fg_color="transparent")
        self._section_playlists.pack(fill="x", pady=(16, 0))

        pl_lbl = ctk.CTkLabel(
            self._section_playlists,
            text="Playlists",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["text_primary"],
            anchor="w",
        )
        pl_lbl.pack(fill="x", pady=(0, 12))

        PlaylistsSection(self._section_playlists, self.colors).pack(fill="x")

    # ── Callbacks ───────────────────────────────
    def _on_tab_change(self, tab: str):
        """Affiche/masque les sections selon l'onglet actif."""
        if tab == "videos":
            self._section_videos.pack(fill="x")
            self._section_playlists.pack_forget()
        else:
            self._section_videos.pack_forget()
            self._section_playlists.pack(fill="x")

