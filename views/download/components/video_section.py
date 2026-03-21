import customtkinter as ctk
from .video_card import VideoCard


class VideosSection(ctk.CTkFrame):
    """Liste des vidéos téléchargées."""

    SAMPLE_DATA = [
        dict(
            title="UNDERWORLD - KATANA (Techno)",
            duration="5:44",
            quality="1080p",
            speed="2.1 MiB/s",
            time_ago="0min ago",
            badge_text="3:44",
        ),
        # dict(
        #     title="What Elon Musk said to invest in 2024",
        #     duration="6:34",
        #     quality="720p",
        #     speed="1.9 MiB/s",
        #     time_ago="8min ago",
        #     badge_text="7:20",
        # ),
        # dict(
        #     title="Souvenir du futur",
        #     duration="8:03",
        #     quality="480p",
        #     speed="1552KB/s",
        #     time_ago="14 min ago",
        #     badge_text="8:03",
        # ),
    ]

    def __init__(self, parent, colors: dict, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.colors = colors
        self._build()

    def _build(self):
        for i, data in enumerate(self.SAMPLE_DATA):
            card = VideoCard(self, self.colors, **data)
            card.pack(fill="x", pady=(0, 10))
