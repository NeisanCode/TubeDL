# 🎬 TubeDL

> Téléchargeur de vidéos YouTube et de playlists, gratuit et open-source.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Licence](https://img.shields.io/badge/licence-MIT-green)
![Status](https://img.shields.io/badge/status-actif-brightgreen)
![Python](https://img.shields.io/badge/python-3.10+-yellow)

## 📋 Sommaire

- [À propos](#-à-propos)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Configuration](#-configuration)
- [Contribution](#-contribution)
- [Licence](#-licence)

---

## 📖 À propos

TubeDL est un téléchargeur de vidéos YouTube open-source, conçu pour être simple, rapide et sans aucune limite.

De nombreux logiciels similaires sont payants, ou leurs versions gratuites limitent le nombre de téléchargements. TubeDL résout ce problème en offrant une solution entièrement gratuite, open-source, et sans restriction — pour télécharger autant de vidéos et de playlists que tu le souhaites.

**Fonctionnalités :**

- ✅ Téléchargement de vidéos en plusieurs qualités (4K, 1080p, 720p...)
- ✅ Téléchargement de playlists complètes
- ✅ Extraction audio (MP3, WAV...)
- ✅ Téléchargement des sous-titres
- ✅ Gratuit et open-source
- ✅ Disponible sur Windows et Linux

---

## ⚡ Installation

### 👤 Utilisateurs — Télécharger l'application

Télécharge la dernière version selon ton système :


| Système | Fichier            |
| ------- | ------------------ |
| Windows | `TubeDL-setup.exe` |
| Linux   | `TubeDL.AppImage`  |


👉 [Voir toutes les releases](https://github.com/NeisanCode/TubeDL/releases)

---

### 🧑‍💻 Développeurs — Lancer depuis le code source

**Prérequis :**

- [Python 3.10+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/#installation)
- FFmpeg (voir ci-dessous)

**Installer FFmpeg :**

Windows (avec [Winget](https://learn.microsoft.com/fr-fr/windows/package-manager/winget/)) :

```bash
winget install ffmpeg
```

Linux (Debian/Ubuntu) :

```bash
sudo apt install ffmpeg
```

Linux (Arch) :

```bash
sudo pacman -S ffmpeg
```

> 💡 FFmpeg est détecté automatiquement par TubeDL via le PATH système — aucune configuration manuelle nécessaire.

**1. Cloner le dépôt**

```bash
git clone https://github.com/NeisanCode/TubeDL.git
cd TubeDL
```

**2. Installer les dépendances**

```bash
uv sync
```

**3. Lancer en mode développement**

```bash
uv run main.py
```

---

### 📦 Compiler l'application

**Prérequis :** avoir suivi les étapes d'installation développeur ci-dessus.

```bash
# Installer PyInstaller
uv pip install pyinstaller

# Compiler
pyinstaller --onefile --windowed main.py
```

L'exécutable sera généré dans le dossier `dist/`.

> 💡 TubeDL utilise [yt-dlp](https://github.com/yt-dlp/yt-dlp) en backend pour le téléchargement.

---

## 💡 Utilisation

### Télécharger une vidéo

Lance l'application, colle l'URL de la vidéo YouTube et choisis la qualité souhaitée.

```
https://www.youtube.com/watch?v=XXXXXXXXX
```

### Télécharger une playlist

Fonctionne de la même façon — colle simplement l'URL de la playlist :

```
https://www.youtube.com/playlist?list=XXXXXXXXX
```

### Extraire l'audio uniquement

Sélectionne le format **MP3** ou **WAV** avant de lancer le téléchargement.

> ⚠️ TubeDL est destiné à un usage personnel. Respecte les conditions d'utilisation de YouTube et le droit d'auteur.

---

## ⚙️ Configuration

La configuration se fait via le fichier `settings.json` généré automatiquement au premier lancement.


| Clé               | Description                                                 | Valeur par défaut                                                  |
| ----------------- | ----------------------------------------------------------- | ------------------------------------------------------------------ |
| `download_folder` | Dossier de téléchargement des vidéos                        | Windows : `C:\Users\<user>\Videos` / Linux : `/home/<user>/Videos` |
| `cookie_file`     | Chemin vers un fichier de cookies (pour les vidéos privées) | `""` (désactivé)                                                   |
| `theme`           | Thème de l'interface (`Light`, `Dark`, `System`)            | `System`                                                           |


**Exemple de fichier `settings.json` :**

```json
{
  "download_folder": "/home/user/Videos",
  "cookie_file": ["", false],
  "theme": "System"
}
```

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment participer :

1. **Fork** le projet
2. Crée ta branche : `git checkout -b feature/ma-feature`
3. Commit tes changements : `git commit -m 'feat: ajout de ma feature'`
4. Push : `git push origin feature/ma-feature`
5. Ouvre une **Pull Request**

### Convention de commits


| Préfixe     | Usage                   |
| ----------- | ----------------------- |
| `feat:`     | Nouvelle fonctionnalité |
| `fix:`      | Correction de bug       |
| `docs:`     | Documentation           |
| `refactor:` | Refactoring du code     |


---

## 📄 Licence

Ce projet est sous licence **MIT** — voir le fichier [LICENSE](LICENSE) pour les détails.

---

Fait avec ❤️ par [NeisanCode](https://github.com/NeisanCode)