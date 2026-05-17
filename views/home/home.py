from logging import root
from queue import Queue
from PIL import Image

import customtkinter as ctk
from controllers import Controller
from controllers.controller import Controller
from models import Video, Short, Playlist
from views.themes.color import BG_INPUT, BG_OUTER
from .components import VideoCard, PlaylistCard, SearchBar


class Home(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TubeDL")
        self.attributes("-zoomed", True)
        self.configure(fg_color=BG_OUTER)
        MID_SIZE = "900x600"

        def on_minimize(event):
            if self.state() == "iconic":  # fenêtre minimisée
                self.after(100, lambda: self.geometry(MID_SIZE))

        self.bind("<Unmap>", on_minimize)
        # Création et affichage de la SearchBar
        self.search_bar = SearchBar(
            self,
            placeholder="  Enter the YouTube URL",
            on_search=self.handle_search,
            on_download=self.handle_download,
        )
        self.search_bar.pack(fill="x", padx=20, pady=20)

        # Création d'un cadre pour les cartes
        self.download_frame = ctk.CTkScrollableFrame(self, fg_color=BG_INPUT)
        self.download_frame.pack(fill="both", expand=True)

    def handle_search(self, query):
        if not query:
            return
        return Controller.analyse_url(query)

    def handle_download(self, media: Video | Short | Playlist, quality):
        print(f"Download {media} in {quality}")
        queue = Queue()
        card = VideoCard(
            self.download_frame,
            title=media.title,
            quality=quality,
            duration=media.duration,
            preview_image=media.pil_thumbnail,
            queue=queue,
            on_download=lambda q: Controller.download(media, q),
        )
        card.pack(fill="x", padx=20, pady=5)
