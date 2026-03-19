import customtkinter as ctk
from .preview_frame import PreviewFrame
from .quality_frame import QualityFrame
from .download_btn import DownloadButton
from models import Playlist, Short, Video


class ContentContainer(ctk.CTkFrame):
    def __init__(self, parent, colors, on_download):
        super().__init__(parent, fg_color="transparent")
        self.colors = colors
        self.on_download = on_download
        self.create_widgets()

    def create_widgets(self):
        self.preview_frame = PreviewFrame(self, self.colors)
        self.preview_frame.grid(row=0, column=0, padx=(0, 20))

        self.quality_frame = QualityFrame(self, self.colors)
        self.quality_frame.grid(row=0, column=1, sticky="nsew")

        self.download_btn = DownloadButton(self, self.colors, command=self.on_download)
        self.download_btn.grid(
            row=2,
            column=0,
            sticky="ew",
            columnspan=2,
            pady=(15, 30),
        )
        self.setsate_btn()

    def update_children(self, media: Video | Playlist | Short):
        self.preview_frame.set_image(media.thumbnail)
        # self.quality_frame.set_resols(media.resols)
    def setsate_btn(self):
        self.download_btn.set_state("normal")

    def get_current_res(self):
        return self.quality_frame.get_resols()
