import customtkinter as ctk


class HeaderFrame(ctk.CTkFrame):
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
