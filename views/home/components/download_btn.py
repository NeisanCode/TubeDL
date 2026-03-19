import customtkinter as ctk


class DownloadButton(ctk.CTkButton):
    def __init__(self, parent, colors, command):
        self.colors = colors
        self.click = 0
        super().__init__(
            parent,
            text="⬇️ TÉLÉCHARGER",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=55,
            corner_radius=12,
            fg_color="#5a5a5a",
            state="disabled",
            command=command,
        )

    def set_state(self, state):
        fg_color = self.colors["accent_primary"] if state == "normal" else "grey"
        cursor = "hand2" if state == "normal" else ""
        self.configure(
            fg_color=fg_color,
            hover_color=self.colors["accent_hover"],
            cursor=cursor,
            state=state,
        )
