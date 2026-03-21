import customtkinter as ctk
from .speed_badge import SpeedBadge
from .video_thumbnail import VideoThumbnail



class VideoCard(ctk.CTkFrame):
    """
    Carte représentant une vidéo téléchargée.

    Paramètres
    ----------
    title       : titre de la vidéo
    duration    : durée (ex. "5:44")
    quality     : qualité (ex. "1080p")
    speed       : vitesse de dl (ex. "2.1 MiB/s")
    time_ago    : temps écoulé (ex. "0min ago")
    badge_text  : texte dans le badge bleu (ex. "3:44")
    """

    def __init__(
        self,
        parent,
        colors: dict,
        title: str,
        duration: str,
        quality: str,
        speed: str,
        time_ago: str,
        badge_text: str,
        **kwargs,
    ):
        super().__init__(
            parent,
            fg_color=colors["bg_secondary"],
            corner_radius=12,
            border_width=1,
            border_color=colors["border"],
            height=88,
            **kwargs,
        )
        self.pack_propagate(False)
        self.colors = colors
        self._build(title, duration, quality, speed, time_ago, badge_text)

    def _build(self, title, duration, quality, speed, time_ago, badge_text):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Thumbnail
        self.thumb = VideoThumbnail(
            self,
            self.colors,
            duration=duration.split("·")[0].strip(),
            width=88,
            height=64,
        )
        self.thumb.grid(row=0, column=0, padx=(12, 10), pady=12, sticky="w")

        # Infos centre
        info_frame = ctk.CTkFrame(self, fg_color="transparent")
        info_frame.grid(row=0, column=1, sticky="nsew", pady=10)
        info_frame.grid_rowconfigure((0, 1), weight=1)

        title_lbl = ctk.CTkLabel(
            info_frame,
            text=title,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=self.colors["text_primary"],
            anchor="w",
        )
        title_lbl.grid(row=0, column=0, sticky="w")

        meta_frame = ctk.CTkFrame(info_frame, fg_color="transparent")
        meta_frame.grid(row=1, column=0, sticky="w")

        dur_lbl = ctk.CTkLabel(
            meta_frame,
            text=duration,
            font=ctk.CTkFont(size=11),
            text_color=self.colors["text_secondary"],
        )
        dur_lbl.pack(side="left")

        sep = ctk.CTkLabel(
            meta_frame,
            text=" · ",
            font=ctk.CTkFont(size=11),
            text_color=self.colors["text_secondary"],
        )
        sep.pack(side="left")

        qual_lbl = ctk.CTkLabel(
            meta_frame,
            text=quality,
            font=ctk.CTkFont(size=11),
            text_color=self.colors["text_secondary"],
        )
        qual_lbl.pack(side="left")

        check_lbl = ctk.CTkLabel(
            meta_frame,
            text="  ✓",
            font=ctk.CTkFont(size=12),
            text_color=self.colors["success"],
        )
        check_lbl.pack(side="left")

        # Vitesse + badge droite
        right_frame = ctk.CTkFrame(self, fg_color="transparent")
        right_frame.grid(row=0, column=2, padx=12, pady=10, sticky="e")

        speed_lbl = ctk.CTkLabel(
            right_frame,
            text=speed,
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=self.colors["text_primary"],
        )
        speed_lbl.pack(anchor="center")

        time_lbl = ctk.CTkLabel(
            right_frame,
            text=time_ago,
            font=ctk.CTkFont(size=10),
            text_color=self.colors["text_secondary"],
        )
        time_lbl.pack(anchor="center")

        badge = SpeedBadge(right_frame, self.colors, text=badge_text)
        badge.pack(anchor="center", pady=(6, 0))
