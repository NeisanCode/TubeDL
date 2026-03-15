import customtkinter as ctk

from view.screen.widget.home import (
    ContentContainer,
    DownloadButton,
    HeaderFrame,
    SearchBarFrame,
)


class HomePage(ctk.CTkFrame):
    """Classe principale qui assemble tous les composants"""

    def __init__(self, parent, colors):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.quality_var = ctk.StringVar(value="maximum")
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = HeaderFrame(self, self.colors)
        self.header.grid(row=0, column=0, sticky="ew", pady=(0, 20))

        # Container principal
        self.main_container = ctk.CTkFrame(self, fg_color="transparent", width=300)
        self.main_container.grid(row=1, column=0, sticky="n")


        # Barre de recherche
        self.search_bar = SearchBarFrame(self.main_container, self.colors)
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
