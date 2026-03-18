import customtkinter as ctk
import CTkMessagebox
from .components import ContentContainer
from .components import DownloadButton
from .components import SearchBarFrame
from models import Video
from models import Playlist
from models import Short
from controllers import Controller
from views.shared import Loader
from views.utils import converto_img

class HomePage(ctk.CTkFrame):
    """Classe principale qui assemble tous les composants"""
    def __init__(self, parent, colors):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.result: Video | Playlist | Short = None
        self.quality_var = ctk.StringVar(value="maximum")
        self.spinner = ctk.CTkProgressBar(
            self,
            mode="indeterminate",
            width=200,
            progress_color=self.colors["accent_primary"],
        )
        self.loading_label = ctk.CTkLabel(self, text="Analyse en cours...")

        self.loader = Loader(
            self,
            self.spinner,
            self.loading_label,
            on_start=lambda: self.search_bar.set_state("disabled"),
            on_finish=self.handle_result,
        )
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # Header
        # self.header = HeaderFrame(self, self.colors)
        # self.header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        # Container principal
        self.main_container = ctk.CTkFrame(self, fg_color="transparent", width=300)
        self.main_container.grid(row=1, column=0, pady=(20, 0), sticky="n")

        # Barre de recherche
        self.search_bar = SearchBarFrame(
            self.main_container,
            self.colors,
            lambda url: self.on_search_click(url),
        )
        self.search_bar.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        # Conteneur de contenu (aperçu + qualité)
        self.content = ContentContainer(
            self.main_container, self.colors, self.quality_var
        )
        self.content.grid(row=1, column=0, sticky="ew", pady=(0, 30))
        self.content.grid_columnconfigure(0, weight=3)
        self.content.grid_columnconfigure(1, weight=1)

        # Bouton de téléchargement
        self.download_btn = DownloadButton(self.main_container, self.colors)
        self.download_btn.grid(row=2, column=0, sticky="ew", pady=(0, 30))

    def on_search_click(self, url):
        if not url:
            CTkMessagebox(
                title="Attention !",
                message="La saisie de l'url est obligatoire",
                icon="warning",
            )
            return
        self.loader.show_spinner(Controller.analyse_url, url)

    def on_update_content(self):
        self.result.thumbnail = converto_img(self.result.thumbnail)
        self.content.update_children(self.result)

    def handle_result(self, data):
        self.search_bar.set_state("normal")
        self.result = data if data else None
        self.on_update_content()

    def on_download_click(self, media):
        pass
