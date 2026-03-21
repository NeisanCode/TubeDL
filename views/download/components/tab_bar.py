import customtkinter as ctk


class TabBar(ctk.CTkFrame):
    """Barre d'onglets avec deux boutons toggle."""

    def __init__(self, parent, colors: dict, on_change=None, **kwargs):
        super().__init__(parent, fg_color=colors["bg_card"], corner_radius=10, **kwargs)
        self.colors = colors
        self._on_change = on_change
        self._active = "videos"
        self._build()

    def _build(self):
        self._btn_videos = ctk.CTkButton(
            self,
            text="Vidéos",
            width=110,
            height=34,
            fg_color=self.colors["accent_primary"],
            text_color="#ffffff",
            hover_color=self.colors["accent_hover"],
            corner_radius=8,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=lambda: self._switch("videos"),
        )
        self._btn_videos.pack(side="left", padx=(4, 2), pady=4)

        self._btn_playlists = ctk.CTkButton(
            self,
            text="Playlists",
            width=110,
            height=34,
            fg_color="transparent",
            text_color=self.colors["text_secondary"],
            hover_color=self.colors["border"],
            corner_radius=8,
            font=ctk.CTkFont(size=13),
            command=lambda: self._switch("playlists"),
        )
        self._btn_playlists.pack(side="left", padx=(2, 4), pady=4)

    def _switch(self, tab: str):
        self._active = tab
        if tab == "videos":
            self._btn_videos.configure(
                fg_color=self.colors["accent_primary"],
                text_color="#ffffff",
                font=ctk.CTkFont(size=13, weight="bold"),
            )
            self._btn_playlists.configure(
                fg_color="transparent",
                text_color=self.colors["text_secondary"],
                font=ctk.CTkFont(size=13),
            )
        else:
            self._btn_playlists.configure(
                fg_color=self.colors["accent_primary"],
                text_color="#ffffff",
                font=ctk.CTkFont(size=13, weight="bold"),
            )
            self._btn_videos.configure(
                fg_color="transparent",
                text_color=self.colors["text_secondary"],
                font=ctk.CTkFont(size=13),
            )
        if self._on_change:
            self._on_change(tab)
