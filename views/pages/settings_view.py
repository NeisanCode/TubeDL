import customtkinter as ctk
from tkinter import filedialog
from views.themes.color import *
from core.config import Config


class SettingsView(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._build()

    def _build(self):
        # ── Titre de la page ──────────────────────────────────────────────────
        title_frame = ctk.CTkFrame(self, fg_color="transparent")
        title_frame.pack(fill="x", padx=32, pady=(32, 20))

        ctk.CTkLabel(
            title_frame,
            text="Paramètres",
            font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
            text_color=TEXT_DARK,
        ).pack(side="left")

        # ── Zone des options (Style Cartes épurées) ───────────────────────────
        options_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        options_container.pack(fill="both", expand=True, padx=32, pady=10)

        # 1. PARAMÈTRE : DOSSIER DES VIDÉOS
        self._create_section_title(options_container, "Emplacements de téléchargement")
        self.video_path_var = ctk.StringVar(
            value=getattr(Config, "download_path", "~/Downloads")
        )
        self._create_path_selector(
            options_container,
            "Dossier des Vidéos",
            self.video_path_var,
            self._browse_video_path,
        )

        # 2. PARAMÈTRE : DOSSIER DES PLAYLISTS
        # (Si ta Config sépare déjà les deux, sinon on pointe vers une variable dédiée)
        self.playlist_path_var = ctk.StringVar(
            value=getattr(Config, "download_path", "~/Downloads")
        )
        self._create_path_selector(
            options_container,
            "Dossier des Playlists",
            self.playlist_path_var,
            self._browse_playlist_path,
        )

        # 3. PARAMÈTRE : COOKIES
        self._create_section_title(options_container, "Cookies")
        self._create_cookie_selector(options_container)

        # 4. PARAMÈTRE : THÈME DE L'APPLICATION
        self._create_section_title(options_container, "Apparence")
        self._create_theme_selector(options_container)

    # ── Fonctions Utilitaires d'UI ────────────────────────────────────────────
    def _create_section_title(self, parent, text):
        ctk.CTkLabel(
            parent,
            text=text,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="bold"),
            text_color=PRIMARY_ACCENT,
        ).pack(anchor="w", pady=(20, 10))

    def _create_path_selector(self, parent, label_text, string_var, browse_command):
        card = ctk.CTkFrame(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
        )
        card.pack(fill="x", pady=6)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        ctk.CTkLabel(
            inner,
            text=label_text,
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="normal"),
            text_color=TEXT_DARK,
        ).pack(side="left")

        # Bouton Parcourir
        ctk.CTkButton(
            inner,
            text="Parcourir...",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color=BG_INPUT,
            text_color=TEXT_DARK,
            hover_color=BORDER,
            width=90,
            height=32,
            corner_radius=6,
            cursor="hand2",
            command=browse_command,
        ).pack(side="right", padx=(10, 0))

        # Affichage du chemin actuel
        ctk.CTkEntry(
            inner,
            textvariable=string_var,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="transparent",
            border_width=0,
            text_color=TEXT_GRAY,
            state="readonly",
            justify="right",
        ).pack(side="right", fill="x", expand=True)

    def _create_cookie_selector(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
        )
        card.pack(fill="x", pady=6)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        # ── Ligne 1 : Label + Toggle ──────────────────────────────────────────
        top_row = ctk.CTkFrame(inner, fg_color="transparent")
        top_row.pack(fill="x")

        ctk.CTkLabel(
            top_row,
            text="Fichier de cookies",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="normal"),
            text_color=TEXT_DARK,
        ).pack(side="left")

        # Conteneur toggle (texte + switch) aligné à droite
        toggle_frame = ctk.CTkFrame(top_row, fg_color="transparent")
        toggle_frame.pack(side="right")

        self._cookie_auto_label = ctk.CTkLabel(
            toggle_frame,
            text="Automatique",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color=TEXT_GRAY,
        )
        self._cookie_auto_label.pack(side="left", padx=(0, 6))

        self._cookie_auto_var = ctk.BooleanVar(
            value=getattr(Config, "cookie_auto", True)
        )
        self._cookie_toggle = ctk.CTkSwitch(
            toggle_frame,
            text="",
            variable=self._cookie_auto_var,
            onvalue=True,
            offvalue=False,
            width=40,
            height=20,
            command=self._on_cookie_toggle,
            cursor="hand2",
        )
        self._cookie_toggle.pack(side="left")

        # ── Ligne 2 : Sélecteur de chemin (masqué si auto) ───────────────────
        self._cookie_path_row = ctk.CTkFrame(inner, fg_color="transparent")
        self._cookie_path_row.pack(fill="x", pady=(10, 0))

        self.cookie_path_var = ctk.StringVar(value=getattr(Config, "cookie_path", ""))

        ctk.CTkButton(
            self._cookie_path_row,
            text="Parcourir...",
            font=ctk.CTkFont(family="Segoe UI", size=12, weight="bold"),
            fg_color=BG_INPUT,
            text_color=TEXT_DARK,
            hover_color=BORDER,
            width=90,
            height=32,
            corner_radius=6,
            cursor="hand2",
            command=self._browse_cookie_path,
        ).pack(side="right", padx=(10, 0))

        ctk.CTkEntry(
            self._cookie_path_row,
            textvariable=self.cookie_path_var,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="transparent",
            border_width=0,
            text_color=TEXT_GRAY,
            state="readonly",
            justify="right",
            placeholder_text="Aucun fichier sélectionné",
        ).pack(side="right", fill="x", expand=True)

        # Appliquer l'état initial
        self._on_cookie_toggle()

    def _create_theme_selector(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
        )
        card.pack(fill="x", pady=6)

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        ctk.CTkLabel(
            inner,
            text="Mode de l'application",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="normal"),
            text_color=TEXT_DARK,
        ).pack(side="left")

        # Menu déroulant pour le thème
        theme_menu = ctk.CTkOptionMenu(
            inner,
            values=["Clair (Light)", "Sombre (Dark)", "Système"],
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color=BG_INPUT,
            text_color=TEXT_DARK,
            button_color=BORDER,
            button_hover_color=BG_INPUT,
            dropdown_fg_color=BG_WHITE,
            dropdown_text_color=TEXT_DARK,
            dropdown_hover_color=BG_INPUT,
            corner_radius=6,
            width=140,
            command=self._change_appearance_mode,
        )
        theme_menu.pack(side="right")

        # Initialiser la valeur visible du menu selon le mode actuel
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            theme_menu.set("Clair (Light)")
        elif current_mode == "Dark":
            theme_menu.set("Sombre (Dark)")
        else:
            theme_menu.set("Système")

    # ── Logique des Actions ───────────────────────────────────────────────────
    def _on_cookie_toggle(self):
        """Active/désactive le sélecteur de chemin selon le mode auto."""
        # Garde-fou : les widgets doivent exister avant d'agir
        if (
            not hasattr(self, "_cookie_auto_var")
            or not hasattr(self, "_cookie_auto_label")
            or not hasattr(self, "_cookie_path_row")
        ):
            return

        is_auto = self._cookie_auto_var.get()

        # Mettre à jour le label du toggle
        self._cookie_auto_label.configure(
            text="Automatique" if is_auto else "Manuel",
            text_color=PRIMARY_ACCENT if is_auto else TEXT_DARK,
        )

        # Afficher ou masquer la ligne du chemin
        if is_auto:
            self._cookie_path_row.pack_forget()
            # Config.cookie_auto = True
        else:
            self._cookie_path_row.pack(fill="x", pady=(10, 0))
            # Config.cookie_auto = False

    def _browse_cookie_path(self):
        file_path = filedialog.askopenfilename(
            title="Sélectionner le fichier de cookies",
            filetypes=[
                ("Fichiers texte / Netscape cookies", "*.txt"),
                ("Tous les fichiers", "*.*"),
            ],
        )
        if file_path:
            self.cookie_path_var.set(file_path)
            # Config.cookie_path = file_path

    def _browse_video_path(self):
        directory = filedialog.askdirectory()
        if directory:
            self.video_path_var.set(directory)
            # Tu peux lier cela à ton fichier Config ici :
            # Config.video_download_path = directory

    def _browse_playlist_path(self):
        directory = filedialog.askdirectory()
        if directory:
            self.playlist_path_var.set(directory)
            # Config.playlist_download_path = directory

    def _change_appearance_mode(self, choice):
        if choice == "Clair (Light)":
            ctk.set_appearance_mode("Light")
        elif choice == "Sombre (Dark)":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("System")

        # On force la fenêtre racine (top level) à recalculer les couleurs immédiatement
        self.winfo_toplevel().update()
