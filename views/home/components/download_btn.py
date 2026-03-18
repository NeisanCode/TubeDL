import customtkinter as ctk

class DownloadButton(ctk.CTkButton):
    def __init__(self, parent, colors):
        state = "diseable"
        super().__init__(
            parent,
            text="⬇️ TÉLÉCHARGER",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=55,
            corner_radius=12,
            fg_color=colors["accent_primary"] if state == "enable" else "grey",
            hover_color=colors["accent_hover"],
            cursor="hand2" if state == "enable" else "arrow",
            state=state,
        )
