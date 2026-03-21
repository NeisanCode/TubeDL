import customtkinter as ctk
from .playlist_card import PlaylistCard

class PlaylistsSection(ctk.CTkFrame):
    """Liste des playlists."""

    SAMPLE_PLAYLISTS = [
        dict(
            name="Ma Playlist Techno", video_count="2 Videos", total_duration="2:9:30"
        ),
        dict(name="Espace & Science", video_count="5 Videos", total_duration="23:80"),
        dict(name="Musique Chill", video_count="4 Videos", total_duration="5:580"),
    ]

    def __init__(self, parent, colors: dict, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.colors = colors
        # self._build()

    def _build(self):
        for data in self.SAMPLE_PLAYLISTS:
            card = PlaylistCard(self, self.colors, **data)
            card.pack(fill="x", pady=(0, 10))
