import customtkinter as ctk


class HeaderFrame(ctk.CTkFrame):
    """Classe pour l'en-tête avec le titre et sous-titre"""

    def __init__(self, parent, colors):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="TubeDL",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=self.colors["text_primary"],
        )
        self.title_label.pack(anchor="w")

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Télécharger des videos en hautes resolutions ...",
            font=ctk.CTkFont(size=14),
            text_color=self.colors["text_secondary"],
        )
        self.subtitle_label.pack(anchor="w", pady=(5, 0))


class SearchBarFrame(ctk.CTkFrame):
    """Classe pour la barre de recherche avec bouton intégré"""

    def __init__(self, parent, colors):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)

        # Frame pour simuler un bouton intégré dans l'Entry
        self.url_frame = ctk.CTkFrame(
            self,
            fg_color=self.colors["bg_secondary"],
            corner_radius=10,
            border_width=2,
            border_color=self.colors["border"],
            width=700,
            height=50,
        )
        self.url_frame.grid(row=0, column=0, sticky="n")
        self.url_frame.grid_columnconfigure(0, weight=1)
        self.url_frame.grid_propagate(False)

        # Entry sans bordures
        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            placeholder_text="Collez l'URL YouTube ici...",
            font=ctk.CTkFont(size=14),
            height=46,
            fg_color="transparent",
            border_width=0,
            text_color=self.colors["text_primary"],
        )
        self.url_entry.grid(row=0, column=0, sticky="ew", padx=(10, 50))

        # Bouton de recherche intégré
        self.search_btn = ctk.CTkButton(
            self.url_frame,
            text="🔍",
            width=40,
            height=36,
            corner_radius=8,
            fg_color=self.colors["accent_primary"],
            hover_color=self.colors["accent_hover"],
            font=ctk.CTkFont(size=16, weight="bold"),
            cursor="hand2",
        )
        self.search_btn.place(relx=1.0, rely=0.5, anchor="e", x=-5)

    def get_url(self):
        return self.url_entry.get()


class PreviewFrame(ctk.CTkFrame):
    """Classe pour l'aperçu vidéo"""

    def __init__(self, parent, colors):
        super().__init__(parent, fg_color=colors["bg_card"], corner_radius=15)
        self.colors = colors
        self.grid_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.preview_icon = ctk.CTkLabel(self, text="🎬", font=ctk.CTkFont(size=48))
        self.preview_icon.place(relx=0.5, rely=0.35, anchor="center")

        self.preview_text = ctk.CTkLabel(
            self,
            text="Aperçu de la vidéo",
            font=ctk.CTkFont(size=16),
            text_color=self.colors["text_secondary"],
        )
        self.preview_text.place(relx=0.5, rely=0.55, anchor="center")


class QualityFrame(ctk.CTkFrame):
    """Classe pour les options de qualité"""

    def __init__(self, parent, colors, quality_var):
        super().__init__(parent, fg_color=colors["bg_card"], corner_radius=15)
        self.colors = colors
        self.quality_var = quality_var
        self.create_widgets()

    def create_widgets(self):
        self.quality_title = ctk.CTkLabel(
            self,
            text="Qualité",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["text_primary"],
        )
        self.quality_title.grid(row=0, column=0, padx=(20, 80), pady=10, sticky="ew")

        qualities = [
            ("maximum", "Max"),
            ("1080p", "1080p"),
            ("720p", "720p"),
            ("480p", "480p"),
            ("240p", "240p"),
        ]

        for i, (value, text) in enumerate(qualities):
            option_frame = ctk.CTkFrame(self, fg_color="transparent")
            option_frame.grid(row=i + 1, column=0, padx=20, pady=6, sticky="w")
            option_frame.grid_columnconfigure(1, weight=1)

            radio = ctk.CTkRadioButton(
                option_frame,
                text="",
                variable=self.quality_var,
                value=value,
                fg_color=self.colors["accent_primary"],
                width=20,
                cursor="hand2",
            )
            radio.grid(row=0, column=0, sticky="w")

            label = ctk.CTkLabel(
                option_frame,
                text=text,
                font=ctk.CTkFont(size=13),
                text_color=self.colors["text_primary"],
            )
            label.grid(row=0, column=1, padx=(6, 0), sticky="w")


class ContentContainer(ctk.CTkFrame):
    """Classe pour le conteneur principal (aperçu + qualité)"""

    def __init__(self, parent, colors, quality_var):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.quality_var = quality_var
        self.create_widgets()

    def create_widgets(self):
        # Aperçu vidéo
        self.preview_frame = PreviewFrame(self, self.colors)
        self.preview_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        # Options de qualité
        self.quality_frame = QualityFrame(self, self.colors, self.quality_var)
        self.quality_frame.grid(row=0, column=1, sticky="nsew")


class DownloadButton(ctk.CTkButton):
    """Classe pour le bouton de téléchargement"""

    def __init__(self, parent, colors):
        super().__init__(
            parent,
            text="⬇️ TÉLÉCHARGER",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=55,
            corner_radius=12,
            fg_color=colors["accent_primary"],
            hover_color=colors["accent_hover"],
            cursor="hand2",
        )
