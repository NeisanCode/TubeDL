import threading
from queue import Queue
import customtkinter as ctk
from PIL import Image
from views.themes.color import *


class _BaseCard(ctk.CTkFrame):
    """Carte de base partagée par VideoCard et PlaylistCard."""

    def __init__(
        self,
        parent,
        title: str,
        queue: Queue,
        on_download: callable,
        preview_image: Image.Image,
        tag_text="",
        tag_color=PRIMARY_ACCENT,
        tag_fg="#FFF",
        **kwargs,
    ):
        super().__init__(
            parent,
            fg_color=BG_WHITE,
            corner_radius=12,          # Coins plus arrondis et modernes
            border_width=1,
            border_color=BORDER,       # Bordure douce style SaaS
            **kwargs,
        )
        self._on_download = on_download
        self.queue = queue
        self._build(title, tag_text, tag_color, tag_fg, preview_image)

    def _build(self, title, tag_text, tag_color, tag_fg, preview_image):
        # ── Vignette placeholder ───────────────────────────────────────────────
        self.thumb = ctk.CTkFrame(
            self,
            width=114,
            height=80,
            fg_color=BG_INPUT,
            corner_radius=8,
        )
        self.thumb.pack(side="left", padx=16, pady=14)
        self.thumb.pack_propagate(False)
        
        ctk.CTkLabel(
            self.thumb,
            text="",
            image=ctk.CTkImage(light_image=preview_image, size=(114, 80)),
        ).place(relx=0.5, rely=0.5, anchor="center")

        # ── Infos centre ──────────────────────────────────────────────────────
        self.info = ctk.CTkFrame(self, fg_color="transparent")
        self.info.pack(side="left", fill="both", expand=True, padx=(4, 12), pady=14)

        ctk.CTkLabel(
            self.info,
            text=title,
            font=ctk.CTkFont(family="Segoe UI", size=15, weight="bold"), # Police plus moderne
            text_color=TEXT_DARK,
            anchor="w",
        ).pack(anchor="w")

        self.meta = ctk.CTkFrame(self.info, fg_color="transparent")
        self.meta.pack(anchor="w", pady=(8, 0))

        self._build_meta(tag_text, tag_color, tag_fg)

        # ── Colonne droite : bouton + barre de progression ─────────────────────
        self._dl_col = ctk.CTkFrame(self, fg_color="transparent")
        self._dl_col.pack(side="right", padx=(0, 16), pady=14)

        self.loading_icon = ctk.CTkImage(
            light_image=Image.open("assets/icons/loading.png"), size=(14, 14)
        )

        self._dl_btn = ctk.CTkButton(
            self._dl_col,
            text="En cours...",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color=PRIMARY_ACCENT,
            hover_color=HOVER_ACCENT,
            text_color=TEXT_LIGHT,
            height=34,
            width=150,
            corner_radius=8,
            cursor="hand2",
            image=self.loading_icon,
        )
        self._dl_btn.pack()

        self._progress = ctk.CTkProgressBar(
            self._dl_col,
            width=150,
            height=5,
            progress_color=PROGRESS_BAR_COLOR, # Cyan néon dynamique
            fg_color=BG_INPUT,
            corner_radius=3,
        )
        self._progress.set(0)
        self._start_download()

    def _build_meta(self, tag_text, tag_color, tag_fg):
        pass

    def _start_download(self):
        self._progress.set(0)
        self._progress.pack(pady=(8, 0))
        threading.Thread(target=self._on_download, args=(self.queue,), daemon=True).start()
        self._watch_queue()
    def _watch_queue(self):
            # 1. On vide les messages accumulés dans la queue pour ce cycle
            while not self.queue.empty():
                self._dl_btn.configure(image=None)
                data = self.queue.get_nowait()
                
                # On laisse chaque carte gérer son affichage textuel et visuel
                self._handle_progress_update(data)

            # 2. IMPORTANT : Toujours planifier le prochain check, sans condition !
            self.after(100, self._watch_queue)

    def _handle_progress_update(self, data):
        """Comportement standard : Utilisé par VideoCard."""
        percent = data["percent"]
        speed = data["speed"]
        
        self._progress.set(percent)
        self._dl_btn.configure(text=f"{int(percent * 100)}% • {speed}")
        
        if percent >= 1:
            self._on_done()

    def _on_done(self):
        self._dl_btn.configure(
            state="normal",
            text="✔ Terminé",
            fg_color=SUCCESS_COLOR,
            hover_color=SUCCESS_HOVER,
            image=None
        )