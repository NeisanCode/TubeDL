import customtkinter as ctk
from tkinter import filedialog
from views.themes.color import *
from core import AppSettings


class CookiesCard(ctk.CTkFrame):
    """Encapsulates cookie loading files and automatic/manual states."""

    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
            **kwargs,
        )
        cookie = AppSettings.load_cookie_file()
        self.cookie_path_var = ctk.StringVar(value=cookie[0])
        self.auto_var = ctk.BooleanVar(value=cookie[1])
        self._build_ui()
        self._toggle_state()

    def _build_ui(self):
        inner = ctk.CTkFrame(self, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        # Ligne 1 : Label & Toggle
        top_row = ctk.CTkFrame(inner, fg_color="transparent")
        top_row.pack(fill="x")

        ctk.CTkLabel(
            top_row,
            text="Fichier de cookies",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_DARK,
        ).pack(side="left")

        toggle_frame = ctk.CTkFrame(top_row, fg_color="transparent")
        toggle_frame.pack(side="right")

        self.status_label = ctk.CTkLabel(
            toggle_frame, text="", font=ctk.CTkFont(family="Segoe UI", size=12)
        )
        self.status_label.pack(side="left", padx=(0, 6))

        ctk.CTkSwitch(
            toggle_frame,
            text="",
            variable=self.auto_var,
            onvalue=True,
            offvalue=False,
            width=40,
            height=20,
            command=self._toggle_state,
            cursor="hand2",
        ).pack(side="left")

        # Ligne 2 : Chemin masqué/affiché
        self.path_row = ctk.CTkFrame(inner, fg_color="transparent")

        ctk.CTkButton(
            self.path_row,
            text="Parcourir...",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color=BG_INPUT,
            text_color=TEXT_DARK,
            hover_color=BORDER,
            width=90,
            height=32,
            corner_radius=6,
            cursor="hand2",
            command=self._browse,
        ).pack(side="right", padx=(10, 0))

        ctk.CTkEntry(
            self.path_row,
            textvariable=self.cookie_path_var,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="transparent",
            border_width=0,
            text_color=TEXT_GRAY,
            state="readonly",
            justify="right",
            placeholder_text="Aucun fichier sélectionné",
        ).pack(side="right", fill="x", expand=True)

    def _toggle_state(self):
        is_auto = self.auto_var.get()
        self.status_label.configure(
            text="Automatique" if is_auto else "Manuel",
            text_color=PRIMARY_ACCENT if is_auto else TEXT_DARK,
        )

        if is_auto:
            self.cookie_path_var.set("")  # ✅ Reset l'affichage
            self.path_row.pack_forget()
        else:
            self.path_row.pack(fill="x", pady=(10, 0))

        AppSettings.save_cookie(self.cookie_path_var.get(), is_auto)

    def _browse(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner le fichier de cookies",
            filetypes=[
                ("Fichiers texte / Netscape cookies", "*.txt"),
                ("Tous les fichiers", "*.*"),
            ],
        )
        if not file_path:
            return
        self.cookie_path_var.set(file_path)
        AppSettings.save_cookie(file_path, self.auto_var.get())
