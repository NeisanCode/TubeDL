import customtkinter as ctk

class PreviewFrame(ctk.CTkFrame):
    def __init__(self, parent, colors):
        super().__init__(
            parent,
            fg_color=colors["bg_card"],
            corner_radius=15,
            height=200,
        )
        self.colors = colors
        self.grid_propagate(False)
        self.create_widgets()

    def create_widgets(self):
        self.preview_icon = ctk.CTkLabel(self, text="🎬", font=ctk.CTkFont(size=48))
        self.preview_icon.place(relx=0.5, rely=0.35, anchor="center")

        self.preview_text = ctk.CTkLabel(
            self,
            text="Aperçu de la vidéo",
            font=ctk.CTkFont(size=16),
            text_color=self.colors["text_secondary"],
        )
        self.preview_text.place(relx=0.5, rely=0.55, anchor="center")

    def set_image(self, image):
        self.preview_icon.place_forget()
        self.preview_text.configure(image=image, text="")
