import json
import os
from pathlib import Path


class HelperSettings:
    FILE_PATH = "settings.json"

    @staticmethod
    def _load() -> dict:
        if not os.path.exists(HelperSettings.FILE_PATH):
            return {}
        with open(HelperSettings.FILE_PATH, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}

    @staticmethod
    def _save(data: dict):
        settings = HelperSettings._load()
        settings.update(data)
        with open(HelperSettings.FILE_PATH, "w") as f:
            json.dump(settings, f, indent=4)

    @staticmethod
    def save_folder_path(path: str):
        HelperSettings._save({"download_folder": path})

    @staticmethod
    def save_cookie(path: str, state: bool):
        HelperSettings._save({"cookie_file": [path, state]})

    @staticmethod
    def save_theme(theme: str):
        HelperSettings._save({"theme": theme})

    @staticmethod
    def load_download_folder() -> str:
        return HelperSettings._load().get("download_folder", str(Path.home() / "Downloads"))

    @staticmethod
    def load_cookie_file():
        return HelperSettings._load().get("cookie_file")

    @staticmethod
    def load_default_theme() -> str:
        return HelperSettings._load().get("theme", "system")
