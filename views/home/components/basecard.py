import threading
from queue import Queue

import customtkinter as ctk
from PIL import Image
from .dialog import ConfirmDialog
from views.themes.color import *


class _BaseCard(ctk.CTkFrame):
    """
    Carte de base partagée par VideoCard et PlaylistCard.

    Paramètres
    ----------
    parent      : widget parent
    title       : titre du média
    quality     : ex. "720P"
    duration    : ex. "3:33"
    tag_text    : libellé du badge ("Video" ou "Playlist")
    tag_color   : couleur de fond du badge
    tag_fg      : couleur du texte du badge
    preview_image : image de vignette
    """

    def __init__(
        self,
        parent,
        title: str,
        quality: str,
        duration: str,
        queue: Queue,
        on_download: callable,
        preview_image: Image.Image,
        tag_text="",
        tag_color=BTN_BLACK,
        tag_fg="#FFF",
        **kwargs,
    ):
        super().__init__(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
            **kwargs,
        )
        self._on_download = on_download
        self.queue = queue
        self._build(
            title,
            quality,
            duration,
            tag_text,
            tag_color,
            tag_fg,
            preview_image,
        )

    def _build(
        self,
        title,
        quality,
        duration,
        tag_text,
        tag_color,
        tag_fg,
        preview_image,
    ):
        # ── Vignette placeholder ───────────────────────────────────────────────
        self.thumb = ctk.CTkFrame(
            self,
            width=110,
            height=76,
            fg_color=BG_NONE,
            corner_radius=6,
        )
        self.thumb.pack(side="left", padx=14, pady=12)
        self.thumb.pack_propagate(False)
        ctk.CTkLabel(
            self.thumb,
            text="",
            font=ctk.CTkFont(size=22),
            text_color=BG_BLACK,
            image=ctk.CTkImage(light_image=preview_image, size=(110, 76)),
        ).place(relx=0.5, rely=0.5, anchor="center")

        # ── Durée (droite) ─────────────────────────────────────────────────────
        ctk.CTkLabel(
            self.thumb,
            text=f" {duration} ",
            font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
            text_color=TEXT_LIGHT,
            fg_color=BG_BLACK,
            height=15,
        ).place(relx=1.0, rely=1.0, anchor="se")

        # ── Infos centre ──────────────────────────────────────────────────────
        self.info = ctk.CTkFrame(self, fg_color="transparent")
        self.info.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        ctk.CTkLabel(
            self.info,
            text=title,
            font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"),
            text_color=TEXT_DARK,
            anchor="w",
        ).pack(anchor="w")

        self.meta = ctk.CTkFrame(self.info, fg_color="transparent")
        self.meta.pack(anchor="w", pady=(6, 0))

        ctk.CTkLabel(
            self.meta,
            text=quality,
            font=ctk.CTkFont(family="Helvetica", size=13),
            text_color=TEXT_GRAY,
        ).pack(side="left", padx=(0, 12))

        # Badge type
        ctk.CTkButton(
            self.meta,
            text=tag_text,
            font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
            fg_color=tag_color,
            hover_color=tag_color,
            text_color=tag_fg,
            height=28,
            width=85,
            corner_radius=20,
            # state="disabled",
        ).pack(side="left")

        # ── Colonne droite : bouton + barre de progression ─────────────────────
        self._dl_col = ctk.CTkFrame(self, fg_color="transparent")
        self._dl_col.pack(side="right", padx=(0, 12), pady=10)

        # carte de base, pas de téléchargement en

        self._dl_btn = ctk.CTkButton(
            self._dl_col,
            text="in progress...",
            font=ctk.CTkFont(family="Helvetica", size=12, weight="bold"),
            fg_color=BTN_BLACK,
            hover_color=BTN_BLACK,
            text_color=TEXT_LIGHT,
            height=32,
            width=130,
            corner_radius=8,
            cursor="hand2",
            image=ctk.CTkImage(
                light_image=Image.open("assets/icons/loading.png"), size=(15, 15)
            ),
        )
        self._dl_btn.pack()

        # barre de progression (initialement cachée)
        self._progress = ctk.CTkProgressBar(
            self._dl_col,
            width=130,
            height=6,
            progress_color=BTN_BLACK,
            fg_color=BORDER,
            corner_radius=4,
        )
        self._progress.set(0)
        self._start_download()

    # ── Téléchargement ────────────────────────────────────────────────────────
    def _start_download(self):
        self._progress.set(0)
        self._progress.pack(pady=(6, 0))

        threading.Thread(
            target=self._on_download,
            args=(self.queue,),
            daemon=True,
        ).start()
        self._watch_queue()

    def _watch_queue(self):
        self._dl_btn.configure(image=None)
        while not self.queue.empty():
            data = self.queue.get_nowait()
            percent = data["percent"]
            speed = data["speed"]
            self._progress.set(percent)
            self._dl_btn.configure(text=f"{int(percent * 100)}% • {speed}")
            if percent >= 1:
                self._on_done()
                return
            if percent["status"] == "downloaded":
                ConfirmDialog(self, "This video has already been downloaded. Do you want to download it again?")
                return
        self.after(100, self._watch_queue)

    def _on_done(self):
        self._dl_btn.configure(
            state="normal",
            text="✔ Terminé",
            fg_color="#2AAA5E",
            hover_color="#228855",
            image=None,
        )
