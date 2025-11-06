import json
from pathlib import Path

path = "location.json"


def load_location() -> dict:
    """
    Charge les données depuis location.json.
    Si le fichier n'existe pas ou est vide, crée un dictionnaire vide.
    """
    if not Path(path).exists():
        save_location({}) 
        return {}

    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        save_location({})
        return {}


def save_location(data: dict):
    """
    Sauvegarde un dictionnaire dans location.json
    """
    try:
        existing = {}
        if Path(path).exists():
            with open(path, "r") as f:
                existing = json.load(f)
        existing.update(data)

        with open(path, "w") as f:
            json.dump(existing, f, indent=4)
    except json.JSONDecodeError:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)


a = None
if(a):
    print("é")
else: 
    print("c")