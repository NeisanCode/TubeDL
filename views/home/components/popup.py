import customtkinter as ctk
from views.themes.color import *
import customtkinter as ctk
from PIL import Image
from utils import round_corners


# ══════════════════════════════════════════════════════════════════════════════
class DownloaderPopup(ctk.CTkToplevel):
    """
    Fenêtre modale de prévisualisation + sélection de qualité.

    Paramètres
    -----------------------------------------------------------------------------
    parent      : fenêtre parente
    title       : titre du média à afficher
    qualities   : liste des qualités disponibles
    on_download : callback(quality: str) appelé quand l'utilisateur clique sur
                  Download → c'est l'appelant qui crée les cards et démarre
                  le téléchargement
    """

    def __init__(
        self,
        parent,
        title: str = "",
        preview_image=None,
        qualities=[],
        on_download=None,
    ):
        super().__init__(parent)
        self._title_text = title
        self._preview_image = preview_image
        self._on_download = on_download
        self._qualities = qualities

        self.title("popup")
        self.geometry("480x360")
        self.resizable(False, False)
        self.configure(fg_color=BG_WHITE)
        self.withdraw()  # IMPORTANT
        self._build()
        self._center_on(parent)

    def popup(self):
        self.deiconify()
        self.lift()
        self.focus_force()
        self.grab_set()

    # ── Construction ──────────────────────────────────────────────────────────
    def _build(self):
        body = ctk.CTkFrame(self, fg_color=BG_WHITE)
        body.pack(fill="both", expand=True, padx=24, pady=20)

        # ── Ligne haute : miniature + boutons radio ────────────────────────────
        top_row = ctk.CTkFrame(body, fg_color="transparent")
        top_row.pack(fill="x")

        # Miniature noire avec ▶
        thumb = ctk.CTkFrame(
            top_row,
            width=200,
            height=140,
            fg_color="#111111",
            corner_radius=8,
        )
        thumb.pack(side="left")
        thumb.pack_propagate(False)

        ctk.CTkLabel(
            thumb,
            text="⏵",
            font=ctk.CTkFont(size=44),
            text_color=BG_WHITE,
            image=ctk.CTkImage(light_image=round_corners(self._preview_image), size=(200, 140)),
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Boutons radio qualité
        radio_col = ctk.CTkFrame(top_row, fg_color="transparent")
        radio_col.pack(side="left", padx=(28, 0), pady=4, anchor="n")

        self.quality_var = ctk.StringVar(
            value=self._qualities[0] if self._qualities else ""
        )
        for q in self._qualities:
            ctk.CTkRadioButton(
                radio_col,
                text=q,
                value=q,
                variable=self.quality_var,
                font=ctk.CTkFont(family="Helvetica", size=15),
                text_color="#111111",
                fg_color=BTN_BLACK,
                hover_color="#444",
                border_color="#888",
            ).pack(anchor="w", pady=7)

        # ── Titre du média ─────────────────────────────────────────────────────
        ctk.CTkLabel(
            body,
            text=self._title_text,
            font=ctk.CTkFont(family="Helvetica", size=13),
            text_color=TEXT_GRAY,
            anchor="w",
            wraplength=430,
        ).pack(anchor="w", pady=(14, 0))

        # ── Bouton Download ────────────────────────────────────────────────────
        self.dl_btn = ctk.CTkButton(
            body,
            text="Download",
            font=ctk.CTkFont(family="Helvetica", size=15, weight="bold"),
            fg_color=BTN_BLACK,
            hover_color=HOVER_BTN,
            text_color="#FFF",
            height=44,
            corner_radius=8,
            image=ctk.CTkImage(
                light_image=Image.open("assets/icons/download.png").resize((20, 20)),
                size=(20, 20),
            ),
            command=self._on_click_download,
        )
        self.dl_btn.pack(fill="x", pady=(12, 0))

    # ── Clic Download → ferme le popup et délègue à l'appelant ────────────────
    def _on_click_download(self):
        quality = self.quality_var.get()
        self.destroy()
        if self._on_download:
            self._on_download(quality)

    # ── API publique ───────────────────────────────────────────────────────────
    def get_quality(self) -> str:
        """Retourne la qualité actuellement sélectionnée."""
        return self.quality_var.get()

    # ── Centrage ──────────────────────────────────────────────────────────────
    def _center_on(self, parent):
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - 480) // 2
        y = parent.winfo_y() + (parent.winfo_height() - 360) // 2
        self.geometry(f"480x360+{x}+{y}")
