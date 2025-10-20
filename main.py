import sys
import time
from yt_dlp import YoutubeDL as yt
from colorama import Fore, Style, init
import os
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as tkf


def download_video(url, dir="./"):
    """Télécharge une vidéo et retourne le chemin complet du fichier"""
    options = {
        "extractor_args": {"youtube": ["player_client=android_lite"]},
        "http_headers": {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/118.0.0.0 Safari/537.36"
            )
        },
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b",
        "outtmpl": f"{dir}/%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": False,
        "merge_output_format": "mp4",
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,
    }
    with yt(options) as ydl:
        info = ydl.extract_info(url, download=True)
        filepath = ydl.prepare_filename(info)
        if not filepath.endswith(".mp4"):
            filepath = os.path.splitext(filepath)[0] + ".mp4"
        return os.path.abspath(filepath)


def download_playlist(url, dir="./"):
    """Télécharge une playlist et retourne le dossier contenant les fichiers"""
    options = {
        "format": "bv*+ba/b",
        "outtmpl": f"{dir}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
        "yesplaylist": True,
        "quiet": False,
        "merge_output_format": "mp4",
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,
    }
    with yt(options) as ydl:
        info = ydl.extract_info(url, download=True)
        playlist_dir = os.path.join(
            dir, info.get("title", "playlist_inconnue").replace("/", "_")
        )
        return os.path.abspath(playlist_dir)


def media_path():
    """Ouvre un sélecteur de dossier"""
    home_directory = Path.home()
    return tkf.askdirectory(
        title="Répertoire de téléchargement", initialdir=home_directory
    )


def restart_app(title):
    """Réinitialise l’affichage"""
    print(Fore.LIGHTGREEN_EX + "Redémarrage en cours".center(50, "-"))
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.LIGHTRED_EX + title)
    print("1 - Télécharger une vidéo\n2 - Télécharger une playlist\n3 - Quitter")


def close_app():
    print(Fore.YELLOW + "Fermeture du programme...")
    sys.exit()


title = """╔══════════════════════╗
║  Youtube Downloader  ║
╚══════════════════════╝
"""

init(autoreset=True)
print(Fore.LIGHTRED_EX + title)
print("1 - Télécharger une vidéo\n2 - Télécharger une playlist\n3 - Quitter")

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)
app_actions = {
    "1": lambda url, dir: download_video(url, dir),
    "2": lambda url, dir: download_playlist(url, dir),
    "3": lambda _: close_app(),
}

res_actions = {"o": lambda t: restart_app(t), "n": lambda _: close_app()}

while True:
    choice = input(Fore.LIGHTGREEN_EX + "Choisissez une option (1, 2, 3): ").strip()
    if choice in app_actions:
        if choice != "3":
            url = (
                input("Entrez l’URL  de la video -> ").strip()
                if choice == "1"
                else input("Entrez l’URL de la playlist -> ").strip()
            )
            ask_path = (
                input("Choisir la destination du media ? (o/n) -> " + Style.RESET_ALL)
                .strip()
                .lower()
            )
            directory = media_path() if ask_path == "o" else os.getcwd()
            result_path = app_actions[choice](url, directory)
            print(Fore.LIGHTBLUE_EX + f"\nTéléchargement terminé : {result_path}")
            restart = (
                input(Fore.LIGHTGREEN_EX + "Voulez-vous continuer ? (o/n) -> ")
                .strip()
                .lower()
            )
            if restart in res_actions:
                res_actions[restart](title)
            else:
                close_app()
        else:
            app_actions[choice](None)
    else:
        print(Fore.LIGHTRED_EX + "Choix invalide !!!")
