import customtkinter as ctk
from views.home.components.preview_frame import PreviewFrame
from views.home.components.quality_frame import QualityFrame
from models import Playlist, Short, Video


class ContentContainer(ctk.CTkFrame):
    def __init__(self, parent, colors, quality_var):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.quality_var = quality_var
        self.create_widgets()

    def create_widgets(self):
        self.preview_frame = PreviewFrame(self, self.colors)
        self.preview_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 20))

        self.quality_frame = QualityFrame(self, self.colors, self.quality_var)
        self.quality_frame.grid(row=0, column=1, sticky="nsew")

    def update_children(self, media: Video | Playlist | Short):
        self.preview_frame.set_image(media.thumbnail)
