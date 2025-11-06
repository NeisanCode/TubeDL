import customtkinter as ctk
from PIL import Image, ImageTk


class LabeledEntry(ctk.CTkFrame):
    def __init__(
        self, master, label_text, text_var, placeholder="", font=("calibri", 13)
    ):
        super().__init__(master)
        self.configure(fg_color="transparent", bg_color="transparent")
        self.pack(padx=15, pady=15)
        ctk.CTkLabel(self, text=label_text, font=font).pack(anchor="nw")
        self.entry = ctk.CTkEntry(
            self,
            textvariable=text_var,
            width=250,
            placeholder_text=placeholder,
        )
        self.entry.pack(pady=(5, 0))


class LabeledButton(ctk.CTkFrame):
    def __init__(
        self,
        master,
        button_text,
        command,
        path_var=None,
        font=("calibri", 13),
        image="",
    ):
        super().__init__(master)
        self.configure(fg_color="transparent", bg_color="transparent")
        self.pack()
        self.button = ctk.CTkButton(
            self,
            text=button_text,
            command=command,
            font=font,
            image=image,
            fg_color="#2c7efb",
        )
        self.button.pack(padx=15)
        if path_var:
            self.path_label = ctk.CTkLabel(
                self,
                textvariable=path_var,
                wraplength=250,
                text_color="gray",
            )
            self.path_label.pack(pady=(0, 8))

    def get_button(self):
        return self.button


class ProgressSection(ctk.CTkFrame):
    def __init__(self, master, progress_var, progress_label, font=("calibri", 13)):
        super().__init__(master)
        self.configure(fg_color="transparent", bg_color="transparent")
        self.pack(padx=15, pady=15)
        self.progress_bar = ctk.CTkProgressBar(self, variable=progress_var, width=250)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(0, 5))
        self.progress_label_widget = ctk.CTkLabel(
            self, textvariable=progress_label, font=font
        )
        self.progress_label_widget.pack()


def create_image(path, size=(20, 20)):
    return ctk.CTkImage(dark_image=Image.open(path), size=size)


def create_icon(master, path):
    try:
        icon = ImageTk.PhotoImage(Image.open(path))
        master.wm_iconphoto(True, icon)
    except Exception as e:
        print("Impossible de charger l'icône :", e)
