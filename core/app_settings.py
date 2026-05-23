import json
import os
from pathlib import Path


class AppSettings:
    FILE_PATH = "settings.json"

    @staticmethod
    def _load() -> dict:
        if not os.path.exists(AppSettings.FILE_PATH):
            return {}
        with open(AppSettings.FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    @staticmethod
    def _save(data: dict):
        settings = AppSettings._load()
        settings.update(data)
        with open(AppSettings.FILE_PATH, "w") as f:
            json.dump(settings, f, indent=4)

    @staticmethod
    def save_folder_path(path: str):
        AppSettings._save({"download_folder": path})

    @staticmethod
    def save_cookie(path: str, state: bool):
        AppSettings._save({"cookie_file": [path, state]})

    @staticmethod
    def save_theme(theme: str):
        AppSettings._save({"theme": theme})

    @staticmethod
    def load_download_folder() -> str:
        return AppSettings._load().get("download_folder", str(Path.home() / "Downloads"))

    @staticmethod
    def load_cookie_file():
        return AppSettings._load().get("cookie_file")

    @staticmethod
    def load_default_theme() -> str:
        return AppSettings._load().get("theme", "system")
