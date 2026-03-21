from views.download.utils import make_placeholder_image
import customtkinter as ctk


class VideoThumbnail(ctk.CTkFrame):
    """Miniature vidéo avec durée affichée en bas à gauche."""

    def __init__(
        self,
        parent,
        colors: dict,
        duration: str = "0:00",
        width: int = 90,
        height: int = 60,
        image=None,
    ):
        super().__init__(
            parent,
            fg_color=colors["bg_card"],
            corner_radius=8,
            width=width,
            height=height,
        )
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.colors = colors

        self._img = image or make_placeholder_image(width, height, "#1e3a5f")
        self._img_label = ctk.CTkLabel(
            self, image=self._img, text="", corner_radius=8, fg_color="transparent"
        )
        self._img_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        self._duration_badge = ctk.CTkLabel(
            self,
            text=duration,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#1e3a5f",
            text_color="#ffffff",
            corner_radius=4,
            width=36,
            height=18,
        )
        self._duration_badge.place(relx=0.04, rely=0.72)

    def set_image(self, image):
        self._img_label.configure(image=image)

    def set_duration(self, duration: str):
        self._duration_badge.configure(text=duration)
