import customtkinter as ctk
from views.themes.color import *
from PIL import Image

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, on_change_tab=None, **kwargs):
        super().__init__(
            parent, 
            fg_color=BG_SIDEBAR, 
            width=220, 
            corner_radius=0, # Droite sur toute la hauteur gauche
            **kwargs
        )
        self._on_change_tab = on_change_tab
        self.buttons = {}
        self.pack_propagate(False) # Garde sa largeur fixe de 220px
        self._build()

    def _build(self):
        # ── Logo / Titre de l'application ──────────────────────────────────────
        logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        logo_frame.pack(fill="x", padx=20, pady=(32, 40))

        ctk.CTkLabel(
            logo_frame,
            text="TubeDL",
            font=ctk.CTkFont(family="Segoe UI", size=26, weight="bold"),
            text_color=TEXT_DARK,
            anchor="w"
        ).pack(side="left")

        # ── Boutons de Navigation ──────────────────────────────────────────────
        # Tu pourras ajouter des icônes ici plus tard dans light_image=...
        self._create_nav_button("download", "Téléchargements")
        self._create_nav_button("settings", "Paramètres")

        # Activer le premier onglet par défaut
        self.set_active_tab("download")

    def _create_nav_button(self, tab_id: str, label: str):
        btn = ctk.CTkButton(
            self,
            text=label,
            font=ctk.CTkFont(family="Segoe UI", size=14, weight="normal"),
            height=42,
            anchor="w",
            corner_radius=8,
            border_spacing=4,
            cursor="hand2",
            command=lambda: self._on_click_tab(tab_id)
        )
        btn.pack(fill="x", padx=14, pady=4)
        self.buttons[tab_id] = btn

    def _on_click_tab(self, tab_id: str):
        self.set_active_tab(tab_id)
        if self._on_change_tab:
            self._on_change_tab(tab_id)

    def set_active_tab(self, active_id: str):
        """Met en valeur visuellement l'onglet sélectionné."""
        for tab_id, btn in self.buttons.items():
            if tab_id == active_id:
                # Style Actif Premium (Texte blanc sur fond bleu Tech)
                btn.configure(
                    fg_color=PRIMARY_ACCENT,
                    hover_color=HOVER_ACCENT,
                    text_color=TEXT_LIGHT,
                    border_width=0
                )
            else:
                # Style Inactif Épuré (Fond transparent, discret)
                btn.configure(
                    fg_color="transparent",
                    hover_color=BG_NAV_HOVER,
                    text_color=TEXT_GRAY,
                    border_width=0
                )