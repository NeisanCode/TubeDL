# TubeDL

TubeDL est téléchargeur de video youtube et de playlist

VersionDemo

## Sommaire

- [À propos](#À-propos)
- [Installation](#Installation)
- [Utilisation](#Utilisation)
- [Configuration](#Configuration)
- [Contribution](#Contribution)
- [Licence](#Licence)

## À propos

Ce projet a été crée afin de permettre le téléchargement de video depuis la plateforme youtube,

Il a été crée parce que de nombreux logiciel similaire sont payant ou les versions gratuites ne permettre qu'un certains nombre de téléchargement de video ce projet est donc totalement open-source et permettre à n'importe qui de pouvoir télécharger des video en illimité

# Prérequis

## ⚡ Installation

### 👤 Utilisateurs — Télécharger l'application

Télécharge la dernière version selon ton système :


| Système | Fichier                |
| ------- | ---------------------- |
| Windows | `youtube-dl-setup.exe` |
| macOS   | `youtube-dl.dmg`       |
| Linux   | `youtube-dl.AppImage`  |


👉 [Voir toutes les releases](https://github.com/ton-user/ton-projet/releases)

### 🧑‍💻 Développeurs — Lancer depuis le code source

**Prérequis :** 

- [Python 3.10+](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html)
- [uv](https://docs.astral.sh/uv/#installation)

##### Cloner le dépôt

```bash
    git https://github.com/NeisanCode/TubeDL.git
    cd TubeDL
```

##### Installer les dépendances

```bash
    uv sync
```

##### Lancer en mode développement

```bash
    uv run main.py
```

> 💡 Le projet utilise [yt-dlp](https://github.com/yt-dlp/yt-dlp) en backend.

