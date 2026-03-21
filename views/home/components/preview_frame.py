import customtkinter as ctk
from views.utils.image import converto_img


class PreviewFrame(ctk.CTkFrame):
    def __init__(self, parent, colors):
        super().__init__(
            parent,
            fg_color=colors["bg_card"],
            bg_color="transparent",
            corner_radius=15,
            width=369,
            height=207,
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
            fg_color="transparent",
            bg_color="transparent",
            text_color=self.colors["text_secondary"],
        )
        self.preview_text.place(relx=0.5, rely=0.55, anchor="center")

    def set_image(self, image):
        preview_img = converto_img(image)
        self.preview_icon.place_forget()
        self.preview_text.configure(
            image=preview_img,
            text="▶",
            text_color="#ff6060",
            font=ctk.CTkFont(size=48),
        )
        self.preview_text.place(relx=0.5, rely=0.5, anchor="center")
        self.preview_text.bind("<Enter>", self.on_hover)
        self.preview_text.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self.preview_text.configure(cursor="hand2")
        # self.play_icon.configure(cursor="hand2")

    def on_leave(self, event):
        self.preview_text.configure(cursor="")
