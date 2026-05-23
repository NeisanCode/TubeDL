import customtkinter as ctk
from .popup import DownloaderPopup
from views.themes.color import *
from PIL import Image
from models import Video, Playlist, Short


class SearchBar(ctk.CTkFrame):
    def __init__(
        self,
        parent,
        on_search=None,
        on_download=None,
        placeholder="  Collez le lien YouTube ici...",
        **kwargs,
    ):
        super().__init__(parent, fg_color=BG_NONE, **kwargs)
        self._on_search_callback = on_search
        self._on_download_callback = on_download
        self._placeholder = placeholder
        self._build()

    def _build(self):
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=self._placeholder,
            font=ctk.CTkFont(family="Segoe UI", size=14),
            height=48,
            fg_color=BG_INPUT,
            border_width=1,
            border_color=BORDER,  # Légère bordure d'ancrage
            corner_radius=10,
            text_color=TEXT_DARK,
        )
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda e: self._on_search())

        image = ctk.CTkImage(
            light_image=Image.open("assets/icons/glass.png"), size=(18, 18)
        )

        self.btn = ctk.CTkButton(
            self,
            text=None,
            width=50,
            height=48,
            corner_radius=10,
            fg_color=PRIMARY_ACCENT,  # Utilise l'accent bleu
            hover_color=HOVER_ACCENT,
            command=self._on_search,
            image=image,
            cursor="hand2",
        )
        self.btn.pack(side="left", padx=(10, 0))

    def _on_search(self):
        url = self.entry.get().strip()
        media = self._on_search_callback(url)
        if not media:
            return
        popup = DownloaderPopup(
            self,
            title=media.title,
            preview_image=media.pil_thumbnail,
            qualities=media.res_list if isinstance(media, Video) else [],
            on_download=lambda q: self._on_download_callback(media, q),
        )
        self.after(0, popup.popup)

    def set_loading(self, loading: bool):
        if loading:
            self.btn.configure(state="disabled", text="…", fg_color=BTN_DISABLED)
            self.entry.configure(state="disabled")
        else:
            self.btn.configure(state="normal", text=None, fg_color=PRIMARY_ACCENT)
            self.entry.configure(state="normal")

    def clear(self):
        self.entry.delete(0, "end")
