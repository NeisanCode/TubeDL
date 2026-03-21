import customtkinter as ctk


class QualityFrame(ctk.CTkFrame):
    def __init__(self, parent, colors):
        super().__init__(
            parent,
            fg_color=colors["bg_card"],
            corner_radius=15,
        )
        self.selected = ctk.StringVar()
        self.colors = colors
        self.radio_widgets = []
        self.create_widgets()

    def create_widgets(self):
        self.quality_title = ctk.CTkLabel(
            self,
            text="Qualité",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=self.colors["text_primary"],
        )
        self.quality_title.grid(row=0, column=0, padx=(20, 80), pady=10, sticky="ew")

    def set_resols(self, resols):
        self._clean_radio()
        resols = [(res, res) for res in resols]
        self.selected.set(resols[0][0]) if resols else self.selected.set("")
        for i, (value, text) in enumerate(resols):
            option_frame = ctk.CTkFrame(self, fg_color="transparent")
            option_frame.grid(row=i + 1, column=0, padx=20, pady=6, sticky="w")
            option_frame.grid_columnconfigure(1, weight=1)

            radio = ctk.CTkRadioButton(
                option_frame,
                text="",
                value=value,
                variable=self.selected,
                fg_color=self.colors["accent_primary"],
                width=20,
                cursor="hand2",
            )
            radio.grid(row=0, column=0, sticky="w")

            label = ctk.CTkLabel(
                option_frame,
                text=text,
                font=ctk.CTkFont(size=13),
                text_color=self.colors["text_primary"],
            )
            label.grid(row=0, column=1, padx=(6, 0), sticky="w")
            self.radio_widgets.append(option_frame)

    def _clean_radio(self):
        for widget in self.radio_widgets:
            widget.destroy()
        self.radio_widgets.clear()

    def get_resols(self):
        return self.selected.get()
