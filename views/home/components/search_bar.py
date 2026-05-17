import customtkinter as ctk
from .popup import DownloaderPopup
from views.themes.color import *
from PIL import Image
from models import Video, Playlist, Short


class SearchBar(ctk.CTkFrame):
    """
    Composant barre de recherche.

    Paramètres
    ----------
    parent       : widget parent
    on_search    : callback(url: str) appelé quand l'utilisateur lance la recherche
    placeholder  : texte placeholder du champ
    """

    def __init__(
        self,
        parent,
        on_search=None,
        on_download=None,
        placeholder="  Enter the URL",
        **kwargs,
    ):
        super().__init__(parent, fg_color=BG_NONE, **kwargs)
        self._on_search_callback = on_search
        self._on_download_callback = on_download
        self._placeholder = placeholder
        self._build()

    # ── Construction ──────────────────────────────────────────────────────────
    def _build(self):
        # Champ de saisie
        self.entry = ctk.CTkEntry(
            self,
            placeholder_text=self._placeholder,
            font=ctk.CTkFont(family="Helvetica", size=15),
            height=50,
            fg_color=BG_INPUT,
            border_width=0,
            corner_radius=8,
            text_color=TEXT_DARK,
        )
        self.entry.pack(side="left", fill="x", expand=True, ipady=4)
        self.entry.bind("<Return>", lambda e: self._on_search())

        # Bouton loupe
        image = ctk.CTkImage(
            light_image=Image.open("assets/icons/glass.png"),
            size=(20, 20),
        )
        self.btn = ctk.CTkButton(
            self,
            text=None,
            font=ctk.CTkFont(size=18),
            width=54,
            height=50,
            corner_radius=8,
            fg_color=BTN_BLACK,
            hover_color=HOVER_BTN,
            command=self._on_search,
            image=image,
            cursor="hand2",
        )
        self.btn.pack(side="left", padx=(8, 0))

    # ── Logique ───────────────────────────────────────────────────────────────
    def _on_search(self):
        url = self.entry.get().strip()
        media: Video | Playlist | Short = self._on_search_callback(url)
        if not media:
            return

        popup = DownloaderPopup(
            self,
            title=media.title,
            preview_image=media.pil_thumbnail,
            qualities=media.res_list if isinstance(media, Video) else None,
            on_download=lambda q: self._on_download_callback(media, q),
        )
        self.after(0, lambda: popup.popup())
        
    # ── API publique ──────────────────────────────────────────────────────────
    def get_url(self) -> str:
        """Retourne le contenu actuel du champ."""
        return self.entry.get().strip()

    def set_loading(self, loading: bool):
        """Active/désactive l'état de chargement sur le bouton."""
        if loading:
            self.btn.configure(state="disabled", text="…")
            self.entry.configure(state="disabled")
        else:
            self.btn.configure(state="normal")
            self.entry.configure(state="normal")

    def clear(self):
        """Vide le champ de saisie."""
        self.entry.delete(0, "end")
