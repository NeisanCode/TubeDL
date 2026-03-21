import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, colors, on_nav_click=None):
        super().__init__(parent, width=220, corner_radius=0, fg_color=colors["sidebar"])
        self.colors = colors
        self.on_nav_click = on_nav_click
        self.nav_buttons = {}

        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):
        # Logo
        self.logo_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.logo_frame.grid(row=0, column=0, padx=20, pady=30)

        self.logo_label = ctk.CTkLabel(
            self.logo_frame,
            text="⬇️ TubeDL",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=self.colors["accent_secondary"],
        )
        self.logo_label.pack()

        # Navigation
        self.nav_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.nav_frame.grid(row=1, column=0, sticky="n", padx=10, pady=20)

        nav_items = [
            ("🏠 Home", "home"),
            ("📥 Téléchargements", "downloads"),
            ("❓ À propos", "about"),
            ("⚙️ Parametres", "settings"),
        ]

        for i, (text, key) in enumerate(nav_items):
            btn = ctk.CTkButton(
                self.nav_frame,
                text=text,
                font=ctk.CTkFont(size=14),
                fg_color="transparent",
                text_color=self.colors["sidebar_text"],
                anchor="w",
                height=45,
                corner_radius=10,
                border_width=0,
                command=lambda page=key: self.handle_nav_click(page),
                cursor="hand2",
            )
            btn.pack(fill="x", pady=5)
            self.nav_buttons[key] = btn

        # Mettre en surbrillance le bouton Home par défaut
        self.set_active_button("home")

    def handle_nav_click(self, key):
        self.set_active_button(key)
        if self.on_nav_click:
            self.on_nav_click(key)

    def set_active_button(self, key):
        for k, btn in self.nav_buttons.items():
            if k == key:
                btn.configure(text_color=self.colors["accent_secondary"])
            else:
                btn.configure(text_color=self.colors["sidebar_text"])
