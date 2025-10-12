import sys
import time
from yt_dlp import YoutubeDL as yt
from colorama import Fore, init
import os
from pathlib import Path
import tkinter as tk
import tkinter.filedialog as tkf
import json


def download_video(url):
    options = {
        # ⚠️ Supprimé "force_generic_extractor": True -> peut empêcher yt-dlp d’utiliser le bon extracteur YouTube
        "extractor_args": {"youtube": ["player_client=android_lite"]},
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/118.0.0.0 Safari/537.36"
        },
        "format": "bv*[ext=mp4]+ba[ext=m4a]/b",  # meilleur combo mp4+m4a
        "outtmpl": "%(title)s.%(ext)s",
        "noplaylist": True,
        "quiet": False,  # pour afficher la progression
        "merge_output_format": "mp4",
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,
    }
    with yt(options) as ydl:
        ydl.download([url])


def download_playlist(url):
    options = {
        "format": "bv*+ba/b",
        "outtmpl": "Playlists/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
        "yesplaylist": True,
        "quiet": False,
        "merge_output_format": "mp4",
        "cookiefile": "cookies.txt" if os.path.exists("cookies.txt") else None,
    }
    with yt(options) as ydl:
        ydl.download([url])


def media_path():
    home_directory = Path.home()
    media_path = tkf.askdirectory(
        title="Repertoire de téléchargement", initialdir=home_directory
    )
    return media_path

def restart_app(title):
    print(Fore.LIGHTGREEN_EX + "Redemarrage en cours".center(50, "-"))
    time.sleep(5)
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
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

actions = {
    "1": lambda url: download_video(url),
    "2": lambda url: download_playlist(url),
    "3": lambda _: close_app(),
}
restarter = {"o": lambda t: restart_app(t), "n": lambda _: close_app()}
root = tk.Tk
root.lift

# while True:
#     choice = input(Fore.LIGHTGREEN_EX + "Choisissez une option (1, 2, 3): ").strip()
#     if choice in actions:
#         if choice != "3":
#             url = input("Entrez l’URL de la vidéo ou de la playlist -> ").strip()
#             actions[choice](url)
#             restart = input(Fore.LIGHTGREEN_EX + "Voulez vous continuez ? (o/n) -> ")
#             if restart in restarter:
#                 restarter[restart](title)
#             else:
#                 close_app()
#         else:
#             actions[choice](None)
#     else:
#         print(Fore.LIGHTRED_EX + "Choix invalide !!!")

media_path()
