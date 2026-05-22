from queue import Queue
import customtkinter as ctk
from controllers import Controller
from models import Video, Short, Playlist
from views.themes.color import *

# On remonte d'un cran (..) pour aller dans components
from ..components.search_bar import SearchBar
from ..components.video_card import VideoCard
from ..components.playlist_card import PlaylistCard

class HomeView(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._card_count = 0
        self._build()

    def _build(self):
        # Header
        header = ctk.CTkFrame(self, fg_color="transparent")
        header.pack(fill="x", padx=32, pady=(32, 0))

        ctk.CTkLabel(
            header, text="Tableau de bord",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"), text_color=TEXT_DARK,
        ).pack(side="left")

        ctk.CTkLabel(
            header, text="—  Gestion de vos flux multimédias",
            font=ctk.CTkFont(family="Segoe UI", size=13), text_color=TEXT_GRAY,
        ).pack(side="left", padx=(12, 0), pady=(6, 0))

        # Barre de recherche
        self.search_bar = SearchBar(
            self,
            placeholder="  Coller l'URL YouTube…",
            on_search=self.handle_search,
            on_download=self.handle_download,
        )
        self.search_bar.pack(fill="x", padx=32, pady=(20, 0))

        # Séparateur + compteur file d'attente
        list_header = ctk.CTkFrame(self, fg_color="transparent")
        list_header.pack(fill="x", padx=32, pady=(24, 8))

        ctk.CTkLabel(
            list_header, text="File d'attente",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"), text_color=TEXT_GRAY,
        ).pack(side="left")

        self._count_label = ctk.CTkLabel(
            list_header, text="0", font=ctk.CTkFont(family="Segoe UI", size=11, weight="bold"),
            text_color=TEXT_LIGHT, fg_color=PRIMARY_ACCENT, corner_radius=10, width=24, height=20,
        )
        self._count_label.pack(side="left", padx=(8, 0))

        # Zone de défilement
        self.download_frame = ctk.CTkScrollableFrame(
            self, fg_color="transparent",
            scrollbar_button_color=BORDER, scrollbar_button_hover_color=PRIMARY_ACCENT,
        )
        self.download_frame.pack(fill="both", expand=True, padx=32, pady=(0, 24))

        # État vide
        self._empty_state = ctk.CTkFrame(self.download_frame, fg_color=BG_WHITE, corner_radius=12, border_width=1, border_color=BORDER)
        self._empty_state.pack(fill="x", pady=8)

        ctk.CTkLabel(self._empty_state, text="Aucun téléchargement actif", font=ctk.CTkFont(family="Segoe UI", size=14), text_color=TEXT_GRAY).pack(pady=54)

    def _add_card(self, card):
        if self._card_count == 0:
            self._empty_state.pack_forget()
        card.pack(fill="x", pady=(0, 10))
        self._card_count += 1
        self._count_label.configure(text=str(self._card_count))

    def handle_search(self, query):
        return Controller.analyse_url(query)

    def handle_download(self, media: Video | Short | Playlist, quality):
        queue = Queue()
        if isinstance(media, (Video, Short)):
            card = VideoCard(
                self.download_frame, title=media.title, quality=quality, duration=media.duration,
                preview_image=media.pil_thumbnail, queue=queue,
                on_download=lambda q: Controller.download(media, q),
            )
        else:
            card = PlaylistCard(
                self.download_frame, title=media.title, queue=queue, count=media.count,
                preview_image=media.pil_thumbnail,
                on_download=lambda q: Controller.download(media, q),
            )
        self._add_card(card)