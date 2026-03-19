import customtkinter as ctk


class SearchBarFrame(ctk.CTkFrame):
    def __init__(self, parent, colors, on_search):
        super().__init__(parent, fg_color="transparent")
        self.on_search = on_search
        self.colors = colors
        self.state = True
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.url_frame = ctk.CTkFrame(
            self,
            fg_color=self.colors["bg_secondary"],
            corner_radius=10,
            border_width=2,
            border_color=self.colors["border"],
            width=550,
            height=50,
        )
        self.url_frame.grid(row=0, column=0, sticky="n")
        self.url_frame.grid_columnconfigure(0, weight=1)
        self.url_frame.grid_propagate(False)

        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            placeholder_text="Collez l'URL YouTube ici...",
            font=ctk.CTkFont(size=14),
            height=46,
            fg_color="transparent",
            border_width=0,
            text_color=self.colors["text_primary"],
        )
        self.url_entry.grid(row=0, column=0, sticky="ew", padx=(10, 50))

        self.search_btn = ctk.CTkButton(
            self.url_frame,
            text="🔍",
            width=40,
            height=36,
            corner_radius=8,
            fg_color=self.colors["accent_primary"] if self.state else "grey",
            hover_color=self.colors["accent_hover"] if self.state else "grey",
            font=ctk.CTkFont(size=16, weight="bold"),
            cursor="hand2",
            command=self._trigger_callback,
        )
        self.search_btn.place(relx=1.0, rely=0.5, anchor="e", x=-5)

    def _trigger_callback(self):
        url = self.url_entry.get().strip()
        self.on_search(url)

    def set_state(self, state):
        self.state = True if state == "normal" else False
        self.search_btn.configure(
            state=state,
            fg_color=self.colors["accent_primary"] if self.state else "grey",
            hover_color=self.colors["accent_hover"] if self.state else "grey",
        )
        self.search_btn.configure(state=state)
        self.url_entry.configure(state=state)
