import customtkinter as ctk
from views.themes.color import *
from core import AppSettings


class ThemeSelectorCard(ctk.CTkFrame):
    """Manages the UI layout to update runtime application themes."""

    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
            **kwargs,
        )

        inner = ctk.CTkFrame(self, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        ctk.CTkLabel(
            inner,
            text="Mode de l'application",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_DARK,
        ).pack(side="left")

        self.theme_menu = ctk.CTkOptionMenu(
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
            command=self._change_theme,
        )
        self.theme_menu.pack(side="right")
        self._set_initial_value()

    def _set_initial_value(self):
        mapping = {
            "Light": "Clair (Light)",
            "Dark": "Sombre (Dark)",
            "System": "Système",
        }
        self.theme_menu.set(mapping.get(ctk.get_appearance_mode(), "Système"))

    def _change_theme(self, choice):
        modes = {"Clair (Light)": "Light", "Sombre (Dark)": "Dark"}
        ctk.set_appearance_mode(modes.get(choice, "System"))
        self.winfo_toplevel().update()
        AppSettings.save_theme(modes.get(choice, "System"))
