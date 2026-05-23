import customtkinter as ctk
from tkinter import filedialog
from views.themes.color import *


class PathSelectorCard(ctk.CTkFrame):
    """A card layout managing path selection variables and actions."""

    def __init__(self, parent, label_text, default_path, **kwargs):
        super().__init__(
            parent,
            fg_color=BG_WHITE,
            corner_radius=10,
            border_width=1,
            border_color=BORDER,
            **kwargs,
        )
        self.path_var = ctk.StringVar(value=default_path)
        inner = ctk.CTkFrame(self, fg_color="transparent")
        inner.pack(fill="x", padx=16, pady=12)

        ctk.CTkLabel(
            inner,
            text=label_text,
            font=ctk.CTkFont(family="Segoe UI", size=13),
            text_color=TEXT_DARK,
        ).pack(side="left")
        
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
            command=self._browse,
        ).pack(side="right", padx=(10, 0))

        ctk.CTkEntry(
            inner,
            textvariable=self.path_var,
            font=ctk.CTkFont(family="Segoe UI", size=12),
            fg_color="transparent",
            border_width=0,
            text_color=TEXT_GRAY,
            state="readonly",
            justify="right",
        ).pack(side="right", fill="x", expand=True)

    def _browse(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path_var.set(directory)
