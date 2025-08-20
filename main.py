
import sys
import os
import subprocess
from tkinter import filedialog, Tk
from colorama import Fore, init

init(autoreset=True)
root = Tk()
root.withdraw()
root.attributes("-topmost", True)
print(
    Fore.LIGHTRED_EX
    + """╔══════════════════════════════════╗
║         Youtube Downloader       ║
╚══════════════════════════════════╝"""
)
if getattr(sys, "frozen", False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
print(Fore.RED + "\n\n Options ")
print("1. Télécharger une vidéo")
print("2. Télécharger une playlist")
print("3. Quitter\n\n")


ffmpeg = os.path.join(base_path, "ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe")
try:
    while True:
        media_type = input(Fore.LIGHTBLUE_EX + "Choisissez une option -> ")

        if media_type == "1":
            pattern = "%(title)s.%(ext)s"
            folder = input("Choisir l'emplacement o/n -> ")

            if folder.lower() == "o":
                path = filedialog.askdirectory(title="Sélectionner un dossier")
                if not path:
                    print(
                        Fore.YELLOW + "❗ Aucune sélection, chemin par défaut utilisé."
                    )
                    path = "./videos"
            else:
                path = "./videos"
                print(
                    Fore.YELLOW
                    + "Chemin non sélectionné, le chemin par défaut sera appliqué."
                )

            os.makedirs(path, exist_ok=True)
            output_path = os.path.join(path, pattern)

            url = input("Entrez l'URL de la vidéo -> ")
            command = f'yt-dlp --ffmpeg-location "{ffmpeg}" -f "bestvideo[height<=1080]+bestaudio/best" -o "{output_path}" "{url}"'
            subprocess.run(command, shell=True, check=True)
            print(Fore.LIGHTGREEN_EX + "\n📂 Dossier de téléchargement :")
            print(Fore.LIGHTGREEN_EX + output_path)
            break

        elif media_type == "2":
            pattern = "%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s"
            folder = input("Choisir l'emplacement o/n -> ")

            if folder.lower() == "o":
                path = filedialog.askdirectory(title="Sélectionner un dossier")
                if not path:
                    print(
                        Fore.YELLOW + "❗ Aucune sélection, chemin par défaut utilisé."
                    )
                    path = "./"
            else:
                path = "./"
                print(
                    Fore.YELLOW
                    + "Chemin non sélectionné, le chemin par défaut sera appliqué."
                )

            output_path = os.path.join(path, pattern)

            url = input(Fore.LIGHTBLUE_EX + "Entrez l'URL de la playlist -> ")
            command = (
                f'yt-dlp --ffmpeg-location "{ffmpeg}" --format "bestvideo[height<=1080]+bestaudio/best" '
                '--merge-output-format "mkv" '
                f'--output "{output_path}" '
                "--limit-rate 3M --retries 10 --fragment-retries 10 --socket-timeout 30 "
                "--force-ipv4 --throttled-rate 100K "
                '--user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" '
                '--extractor-args "youtube:skip=hls,dash" '
                '--compat-options "no-youtube-unavailable-videos" '
                "--ignore-errors --no-simulate --console-title --xattr-set-filesize "
                f'"{url}"'
            )
            subprocess.run(command, shell=True, check=True)
            print(Fore.LIGHTGREEN_EX + "\n📂 Dossier de téléchargement :")
            print(Fore.LIGHTGREEN_EX + output_path)
            break

        elif media_type == "3":
            print(Fore.LIGHTBLUE_EX + "Fin du programme.")
            break

        else:
            print(Fore.LIGHTRED_EX + "❌ Choix incorrect, veuillez réessayer.")

except subprocess.CalledProcessError as e:
    print(Fore.LIGHTRED_EX + f"❌ Erreur pendant l'exécution de la commande :\n{e}")
except KeyboardInterrupt:
    print(Fore.LIGHTYELLOW_EX + "\n⛔ Interruption par l'utilisateur.")
except Exception as e:
    print(Fore.LIGHTRED_EX + f"⚠️ Erreur inattendue : {e}")
