import customtkinter as ctk


class SpeedBadge(ctk.CTkLabel):
    """Badge circulaire bleu affichant la durée / progression."""

    def __init__(self, parent, colors: dict, text: str = ""):
        super().__init__(
            parent,
            text=text,
            font=ctk.CTkFont(size=11, weight="bold"),
            fg_color=colors["accent_primary"],
            text_color="#ffffff",
            corner_radius=20,
            width=44,
            height=44,
        )
