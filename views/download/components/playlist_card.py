import customtkinter as ctk
from .video_thumbnail import VideoThumbnail

class PlaylistCard(ctk.CTkFrame):
    """Carte d'une playlist dans la section Playlists."""

    def __init__(
        self,
        parent,
        colors: dict,
        name: str,
        video_count: str,
        total_duration: str,
        on_click=None,
        **kwargs,
    ):
        super().__init__(
            parent,
            fg_color=colors["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=colors["border"],
            height=80,
            **kwargs,
        )
        self.pack_propagate(False)
        self.colors = colors
        self._build(name, video_count, total_duration, on_click)
        self.bind("<Enter>", self._on_hover)
        self.bind("<Leave>", self._on_leave)

    def _build(self, name, video_count, total_duration, on_click):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Thumbnail
        thumb = VideoThumbnail(self, self.colors, width=80, height=56)
        thumb.grid(row=0, column=0, padx=(12, 10), pady=12)

        # Infos
        info = ctk.CTkFrame(self, fg_color="transparent")
        info.grid(row=0, column=1, sticky="nsew")
        info.grid_rowconfigure((0, 1), weight=1)

        name_lbl = ctk.CTkLabel(
            info,
            text=name,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.colors["text_primary"],
            anchor="w",
        )
        name_lbl.grid(row=0, column=0, sticky="w")

        sub_lbl = ctk.CTkLabel(
            info,
            text=f"{video_count}  •  {total_duration}",
            font=ctk.CTkFont(size=11),
            text_color=self.colors["text_secondary"],
            anchor="w",
        )
        sub_lbl.grid(row=1, column=0, sticky="w")

        # Infos droite + chevron
        right = ctk.CTkFrame(self, fg_color="transparent")
        right.grid(row=0, column=2, padx=12)

        count_dur = ctk.CTkLabel(
            right,
            text=f"{video_count}, {total_duration}",
            font=ctk.CTkFont(size=11),
            text_color=self.colors["text_secondary"],
        )
        count_dur.pack(side="left", padx=(0, 6))

        chev = ctk.CTkButton(
            right,
            text="∨",
            width=28,
            height=28,
            fg_color="transparent",
            text_color=self.colors["text_secondary"],
            hover_color=self.colors["bg_card"],
            corner_radius=6,
            command=on_click,
        )
        chev.pack(side="left")

    def _on_hover(self, _):
        self.configure(fg_color=self.colors["bg_card"])

    def _on_leave(self, _):
        self.configure(fg_color=self.colors["bg_secondary"])
