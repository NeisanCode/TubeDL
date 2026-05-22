import customtkinter as ctk
from views.themes.color import *
from PIL import Image
from utils import round_corners

class DownloaderPopup(ctk.CTkToplevel):
    def __init__(self, parent, title: str = "", preview_image=None, qualities=[], on_download=None):
        super().__init__(parent)
        self._title_text = title
        self._preview_image = preview_image
        self._on_download = on_download
        self._qualities = qualities

        self.title("Options de téléchargement")
        self.geometry("500x380")
        self.resizable(False, False)
        self.configure(fg_color=BG_WHITE)
        self.withdraw()
        self._build()
        self._center_on(parent)

    def popup(self):
        self.deiconify()
        self.lift()
        self.focus_force()
        self.grab_set()

    def _build(self):
        body = ctk.CTkFrame(self, fg_color=BG_WHITE)
        body.pack(fill="both", expand=True, padx=24, pady=24)

        top_row = ctk.CTkFrame(body, fg_color="transparent")
        top_row.pack(fill="x")

        # Miniature avec coins arrondis fluides
        thumb = ctk.CTkFrame(top_row, width=210, height=145, fg_color=BG_INPUT, corner_radius=10)
        thumb.pack(side="left")
        thumb.pack_propagate(False)

        ctk.CTkLabel(
            thumb,
            text="",
            image=ctk.CTkImage(light_image=round_corners(self._preview_image), size=(210, 145)),
        ).place(relx=0.5, rely=0.5, anchor="center")

        # Sélection qualité épurée
        radio_col = ctk.CTkFrame(top_row, fg_color="transparent")
        radio_col.pack(side="left", padx=(24, 0), pady=4, anchor="n")

        self.quality_var = ctk.StringVar(value=self._qualities[0] if self._qualities else "")
        for q in self._qualities:
            ctk.CTkRadioButton(
                radio_col,
                text=q,
                value=q,
                variable=self.quality_var,
                font=ctk.CTkFont(family="Segoe UI", size=14),
                text_color=TEXT_DARK,
                fg_color=PRIMARY_ACCENT,
                hover_color=HOVER_ACCENT,
                border_color=TEXT_GRAY,
            ).pack(anchor="w", pady=6)

        # Titre
        ctk.CTkLabel(
            body,
            text=self._title_text,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=TEXT_DARK,
            anchor="w",
            wraplength=450,
        ).pack(anchor="w", pady=(18, 0))

        # Bouton Télécharger Moderne
        self.dl_btn = ctk.CTkButton(
            body,
            text="Lancer le téléchargement",
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            fg_color=PRIMARY_ACCENT,
            hover_color=HOVER_ACCENT,
            text_color=TEXT_LIGHT,
            height=46,
            corner_radius=10,
            command=self._on_click_download,
        )
        self.dl_btn.pack(fill="x", pady=(16, 0))

    def _on_click_download(self):
        quality = self.quality_var.get()
        self.destroy()
        if self._on_download:
            self._on_download(quality)

    def _center_on(self, parent: ctk.CTk):
        parent.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() - 500) // 2
        y = parent.winfo_y() + (parent.winfo_height() - 380) // 2
        self.geometry(f"500x380+{x}+{y}")