"""
TubeDL - YouTube Video Downloader Application

A GUI application for downloading videos and playlists from YouTube and other platforms
using yt-dlp. Built with CustomTkinter for a modern dark-themed interface.

Features:
    - Download single videos or entire playlists
    - Cookie-based authentication support
    - FFmpeg integration for video processing
    - Real-time download progress tracking
    - Persistent storage of file locations
"""

import os
import customtkinter as ctk
import tkfilebrowser
from tkinter import StringVar, filedialog, messagebox
import threading

import yt_dlp
import yt_dlp.utils
from downloader import downloader
from save_location import load_location, save_location
from components import (
    LabeledButton,
    LabeledEntry,
    ProgressSection,
    create_icon,
    create_image,
)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class TubDL(ctk.CTk):
    """
    Main application class for TubeDL video downloader.

    This class manages the GUI interface and handles user interactions for
    downloading videos from various platforms using yt-dlp.

    Attributes:
        location (dict): Stored file paths for download folder, cookies, and FFmpeg
        url_var (StringVar): Variable holding the input URL
        type_var (StringVar): Variable for media type selection (Video/Playlist)
        path_var (StringVar): Display variable for shortened download path
        cookie_path (StringVar): Display variable for shortened cookie file path
        ffmpeg_path (StringVar): Display variable for shortened FFmpeg path
        progress_var (DoubleVar): Progress bar value (0.0 to 1.0)
        progress_label (StringVar): Label for progress status text
    """

    def __init__(self):
        """
        Initialize the TubeDL application window and all UI components.

        Sets up the main window, loads saved locations, initializes variables,
        and creates the three-column layout with input fields, options, and
        required file selectors.
        """
        super().__init__()
        self.title("TubeDL")
        self.geometry("800x500")
        self.resizable(False, False)
        logo = "icons/logo.ico"
        create_icon(self, logo)

        self.location = load_location()
        self.url_var = ctk.StringVar()
        self.type_var = ctk.StringVar(value="Video")

        path_var = self.shorten_path(self.location.get("path", "No Folder selected"))
        self.path_var = ctk.StringVar(value=path_var)

        cookie_path = self.shorten_path(
            self.location.get("cookies", "Cookies not found")
        )
        self.cookie_path = ctk.StringVar(value=cookie_path)

        ffmpeg_path = self.shorten_path(self.location.get("ffmpeg", "FFmpeg not found"))
        self.ffmpeg_path = ctk.StringVar(value=ffmpeg_path)

        self.progress_var = ctk.DoubleVar(value=0)
        self.progress_label = ctk.StringVar()

        main_font = "monospace"  # The Main app font
        label_font = (main_font, 16, "bold")
        self.font = (main_font, 13, "bold")

        # ----- App Logo ------
        bg_label = ctk.CTkLabel(
            self,
            image=create_image(logo, size=(120, 120)),
            text="",
        )
        bg_label.pack()

        # --- Main container ---
        container = ctk.CTkFrame(self, corner_radius=10)
        container.pack(expand=True, padx=20, pady=20)

        # --- Frames ---
        left_frame = ctk.CTkFrame(container, corner_radius=10)
        right_frame = ctk.CTkFrame(container, corner_radius=10)
        last_frame = ctk.CTkFrame(container, corner_radius=10)

        left_frame.grid(row=0, column=0, padx=8, pady=10, sticky="nsew")
        right_frame.grid(row=0, column=1, padx=8, pady=10, sticky="nsew")
        last_frame.grid(row=0, column=2, padx=8, pady=10, sticky="nsew")

        container.grid_columnconfigure((0, 1), weight=1)
        container.grid_rowconfigure(0, weight=1)

        # --- LEFT FRAME ---
        self.entry = LabeledEntry(
            left_frame,
            "Enter a URL",
            self.url_var,
            font=label_font,
            placeholder="https://youtube.com/...",
        )
        self.download_button = ctk.CTkButton(
            left_frame,
            text="Download",
            fg_color="#2c7efb",
            command=self.start_download_thread,
            font=self.font,
            image=create_image("icons/download.png"),
        )
        self.download_button.pack(pady=(0, 10))
        ProgressSection(left_frame, self.progress_var, self.progress_label)

        # --- RIGHT FRAME ---
        ctk.CTkLabel(right_frame, text="Link Type", font=label_font).pack(
            anchor="nw", padx=15, pady=(15, 5)
        )
        ctk.CTkOptionMenu(
            right_frame,
            variable=self.type_var,
            values=["Video", "Playlist"],
            font=self.font,
            dropdown_font=self.font,
        ).pack(padx=15, pady=(0, 15), fill="x")

        self.location_widget = LabeledButton(
            right_frame,
            "Locate directory",
            self.choose_path,
            path_var=self.path_var,
            font=self.font,
            image=create_image("icons/folder.png"),
        )

        # --- BOTTOM FRAME ---
        ctk.CTkLabel(last_frame, text="Required", font=label_font).pack(
            anchor="nw", padx=15, pady=(15, 5)
        )

        self.cookie_widget = LabeledButton(
            last_frame,
            "Locate Cookies",
            self.choose_cookies,
            path_var=self.cookie_path,
            font=self.font,
            image=create_image("icons/cookie.png"),
        )

        self.ffmpeg_widget = LabeledButton(
            last_frame,
            "Locate FFmpeg",
            self.choose_ffmpeg,
            path_var=self.ffmpeg_path,
            font=self.font,
            image=create_image("icons/ffmpeg.png"),
        )

    # --- Path handling ---
    def shorten_path(self, path: str, max_length: int = 25):
        """
        Shorten a file path for display purposes.

        Truncates long paths by keeping the beginning and end, with '...' in the middle.
        Paths shorter than max_length are returned unchanged.

        Args:
            path (str): The full file path to shorten
            max_length (int, optional): Maximum length of the shortened path. Defaults to 25.

        Returns:
            str: The shortened path string

        Example:
            >>> shorten_path("/very/long/path/to/file.txt", 20)
            "/very/l.../file.txt"
        """
        if len(path) <= max_length:
            return path
        part_length = (max_length - 3) // 2
        return path[:part_length] + "..." + path[-part_length:]

    def choose_path(self):
        """
        Open a directory selection dialog and save the chosen path.

        Updates the path display variable and persists the selection
        to storage for future sessions.
        """
        folder = filedialog.askdirectory(title="Select a folder")
        if folder:
            self.path_var.set(self.shorten_path(folder))
            save_location({"path": folder})

    def choose_file(self, var: StringVar, key: str, filetypes: tuple):
        """
        Generic file selection handler.

        Opens a file dialog, updates the display variable, and saves the
        selected file path to persistent storage.

        Args:
            var (StringVar): The variable to update with the shortened path
            key (str): The storage key for saving the file path
            filetypes (tuple): File type filter for the dialog (name, pattern)
        """
        file = filedialog.askopenfilename(filetypes=[filetypes])
        if file:
            var.set(self.shorten_path(file))
            save_location({key: file})

    def choose_cookies(self):
        """
        Open file dialog to select a cookie file (*.txt).

        Cookie files are used for authentication when downloading
        videos that require login.
        """
        filetypes = ("Fichier texte", "*.txt")
        self.choose_file(self.cookie_path, "cookies", filetypes)

    def choose_ffmpeg(self):
        """
        Open file dialog to select the FFmpeg executable.

        Automatically adjusts file type filter based on the operating system:
        - Windows: *.exe files
        - Linux/macOS: All executable files
        """
        if os.name == "posix":  # Linux / macOS
            filetypes = ("Fichiers exécutables FFmpeg", "*")
        else:  # Windows
            filetypes = ("Fichiers exécutables FFmpeg", "*.exe")

        self.choose_file(self.ffmpeg_path, "ffmpeg", filetypes)

    # --- Download ---
    def start_download_thread(self):
        """
        Start the download process in a separate thread.

        Prevents the UI from freezing during downloads by running
        the download_media method in a background thread.
        """
        threading.Thread(target=self.download_media).start()

    def download_media(self):
        """
        Main download handler with validation and error handling.

        Validates all required inputs (URL, paths), disables UI during download,
        calls the downloader function, and handles any errors that occur.

        The UI is automatically re-enabled after download completion or failure
        via the finally block.

        Error Types Handled:
            - yt_dlp.utils.DownloadError: Invalid URLs or download failures
            - Exception: Any unexpected errors during download
        """
        url = self.url_var.get()
        media_type = self.type_var.get()
        path = self.location.get("path")
        cookie_path = self.location.get("cookies")
        ffmpeg_path = self.location.get("ffmpeg")

        errors = {
            not url: "Error: Please enter a valid URL.",
            not path: "Error: Please select a download folder.",
            not cookie_path: "Error: Please select a cookie file.",
            not ffmpeg_path: "Error: Please select the FFmpeg file.",
        }
        for condition, message in errors.items():
            if condition:
                messagebox.showwarning("Error", message)
                return

        self.set_ui_state("disabled")

        try:
            downloader(
                url=url,
                media_type=media_type,
                media_path=path,
                cookie_path=cookie_path,
                ffmpeg_path=ffmpeg_path,
                progress_hook=self.update_progress,
            )
            messagebox.showinfo("Success", f"{media_type} download completed!")
        except yt_dlp.utils.DownloadError as e:
            error_msg = str(e)
            if "is not a valid URL" in error_msg:
                messagebox.showerror(
                    "Invalid URL", "The URL format is invalid or not supported."
                )
            else:
                messagebox.showerror("Download Error", f"Download failed:\n{error_msg}")
            self.progress_var.set(0)
        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An error occurred:\n{str(e)}")
            self.progress_var.set(0)
        finally:
            # Always re-enable UI
            self.set_ui_state("enabled")

    def set_ui_state(self, state):
        """
        Enable or disable all interactive UI elements.

        Used to prevent user interaction during downloads and re-enable
        controls after completion.

        Args:
            state (str): Either "enabled" or "disabled"
        """
        self.download_button.configure(state=state)
        self.location_widget.get_button().configure(state=state)
        self.cookie_widget.get_button().configure(state=state)
        self.ffmpeg_widget.get_button().configure(state=state)
        self.progress_label.set("Download in progress...")

        if state == "enabled":
            self.progress_label.set("")
            self.progress_var.set(0)

    def update_progress(self, d):
        """
        Callback function for yt-dlp download progress updates.

        Updates the progress bar based on download status information
        provided by yt-dlp's progress_hooks.

        Args:
            d (dict): Progress dictionary from yt-dlp containing:
                - status (str): Current status ("downloading" or "finished")
                - total_bytes (int, optional): Total file size in bytes
                - total_bytes_estimate (int, optional): Estimated total size
                - downloaded_bytes (int): Bytes downloaded so far
        """
        if d["status"] == "downloading":
            total = d.get("total_bytes") or d.get("total_bytes_estimate")
            downloaded = d.get("downloaded_bytes", 0)
            if total:
                self.progress_var.set(downloaded / total)
        elif d["status"] == "finished":
            self.progress_var.set(1.0)
            print("Download finished!")


if __name__ == "__main__":
    app = TubDL()
    app.mainloop()
