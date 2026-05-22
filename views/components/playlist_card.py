from queue import Queue
import customtkinter as ctk
from PIL import Image
from utils import round_corners
from .basecard import _BaseCard
from views.themes.color import *


class PlaylistCard(_BaseCard):
    def __init__(
        self,
        parent,
        title: str,
        queue: Queue,
        preview_image=round_corners(Image.open("assets/images/fallback.png")),
        on_download=None,
        count: int = 0,
    ):
        self.count = count
        super().__init__(
            parent,
            title=title,
            queue=queue,
            tag_text="Playlist",
            tag_color=TAG_PLAYLIST,
            tag_fg=TAG_PLAYLIST_FG,
            preview_image=preview_image,
            on_download=on_download,
        )

    def _build_meta(self, tag_text, tag_color, tag_fg):
        # On garde une référence du label pour pouvoir le mettre à jour en direct !
        self.count_label = ctk.CTkLabel(
            self.meta,
            text=f"0 / {self.count} vidéos",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_GRAY,
        )
        self.count_label.pack(side="left", padx=(0, 12))

        ctk.CTkLabel(
            self.meta,
            text=tag_text.upper(),
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            fg_color=tag_color,
            text_color=tag_fg,
            height=22,
            corner_radius=6,
            padx=8,
        ).pack(side="left")

    def _handle_progress_update(self, data):
            """Gestion personnalisée et synchronisée pour les playlists."""
            percent = data["percent"]
            speed = data["speed"]
            current_video = data.get("current_video", 1)
            
            # 1. Calcul et mise à jour de la barre de progression GLOBALE
            global_percent = ((current_video - 1) + percent) / self.count
            self._progress.set(global_percent)
            
            # 2. Synchronisation des textes UI
            self.count_label.configure(text=f"{current_video} / {self.count} vidéos")
            self._dl_btn.configure(text=f"V{current_video} : {int(percent * 100)}% • {speed}")
            
            # 3. Validation de la fin réelle de la playlist
            if current_video >= self.count and percent >= 1:
                self._on_done()