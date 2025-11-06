import customtkinter as ctk
from tkinter import filedialog, messagebox
import threading
import yt_dlp

from downloader import downloader

# --- Global configuration ---
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")


class TubDL(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TubeDL")
        self.geometry("600x400")
        self.resizable(False, False)

        # Variables
        self.url_var = ctk.StringVar()
        self.type_var = ctk.StringVar(value="Video")
        self.path_var = ctk.StringVar(value="No folder selected")
        self.progress_var = ctk.DoubleVar(value=0)
        main_font = "calibri"
        self.title_font = (main_font, 16, "bold")
        self.font = (main_font, 13, "bold")

        # --- Main container ---
        container = ctk.CTkFrame(self, corner_radius=10)
        container.pack(expand=True, padx=20, pady=20)

        # --- Left and right frames ---
        left_frame = ctk.CTkFrame(container, corner_radius=10)
        right_frame = ctk.CTkFrame(container, corner_radius=10)

        left_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")
        right_frame.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        container.grid_columnconfigure((0, 1), weight=1)
        container.grid_rowconfigure(0, weight=1)

        # === LEFT FRAME ===
        url_label = ctk.CTkLabel(left_frame, text="Enter a URL", font=self.title_font)
        url_label.pack(anchor="nw", padx=(15, 5), pady=(15, 5))

        url_entry = ctk.CTkEntry(
            left_frame,
            textvariable=self.url_var,
            width=250,
            placeholder_text="https://youtube.com/...",
        )
        url_entry.pack(padx=(15, 15), pady=(0, 15))

        self.download_button = ctk.CTkButton(
            left_frame,
            text="Download",
            fg_color="#2c7efb",
            command=self.start_download_thread,
            font=self.font,
        )
        self.download_button.pack(pady=(0, 20))

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(
            left_frame, variable=self.progress_var, width=250
        )
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(0, 10))

        # === RIGHT FRAME ===
        type_label = ctk.CTkLabel(right_frame, text="Link Type", font=self.title_font)
        type_label.pack(anchor="nw", padx=(15, 5), pady=(15, 5))

        type_menu = ctk.CTkOptionMenu(
            right_frame,
            variable=self.type_var,
            values=["Video", "Playlist"],
            font=self.font,
            dropdown_font=self.font,
        )
        type_menu.pack(pady=(0, 15))

        path_button = ctk.CTkButton(
            right_frame,
            text="Locate directory",
            command=self.choose_path,
            font=self.font,
        )
        path_button.pack(padx=(15, 15), pady=(0, 10))

        self.path_label = ctk.CTkLabel(
            right_frame,
            textvariable=self.path_var,
            wraplength=250,
            text_color="gray",
            font=self.font,
        )
        self.path_label.pack(pady=(0, 10))

    # --- Path handling ---
    def shorten_path(self, path: str, max_length: int = 40):
        if len(path) <= max_length:
            return path
        else:
            part_length = (max_length - 3) // 2
            return path[:part_length] + "..." + path[-part_length:]

    def choose_path(self):
        folder = filedialog.askdirectory(title="Select a folder")
        if folder:
            short = self.shorten_path(folder, 30)
            self.path_var.set(short)

    # --- Download ---
    def start_download_thread(self):
        # Run download in a separate thread to avoid freezing the GUI
        thread = threading.Thread(target=self.download_media)
        thread.start()

    def download_media(self):
        url = self.url_var.get().strip()
        media_type = self.type_var.get()
        path = self.path_var.get()

        if not url:
            messagebox.showwarning("Error", "Please enter a valid URL.")
            return
        if path == "No folder selected":
            messagebox.showwarning("Error", "Please select a download folder.")
            return
        self.download_button.configure(state="disabled")
        try:
            downloader(url, media_type, path, self.update_progress)
            messagebox.showinfo("Download", f"{media_type} download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"Download failed:\n{str(e)}")
            self.progress_var.set(0)

    def update_progress(self, d):
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if total:
                progress = downloaded / total
                self.progress_var.set(progress)
        elif d["status"] == "finished":
            self.progress_var.set(1.0)
            print("Download finished!")


if __name__ == "__main__":
    app = TubDL()
    app.mainloop()
