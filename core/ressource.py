import shutil
import subprocess
import platform


def check_dependencies() -> dict:
    """Vérifie les dépendances nécessaires"""
    return {
        "ffmpeg": shutil.which("ffmpeg") is not None,
        "winget": shutil.which("winget") is not None,
    }


def install_ffmpeg() -> bool:
    """Installe ffmpeg via winget et recharge le PATH"""
    try:
        subprocess.run(
            [
                "winget",
                "install",
                "ffmpeg",
                "--accept-source-agreements",
                "--accept-package-agreements",
            ],
            check=True,
        )
        _refresh_path()
        return shutil.which("ffmpeg") is not None
    except subprocess.CalledProcessError:
        return False


def _refresh_path():
    """Recharge le PATH Windows sans redémarrer"""
    import winreg
    import os

    paths = []
    for hive, subkey in [
        (
            winreg.HKEY_LOCAL_MACHINE,
            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
        ),
        (winreg.HKEY_CURRENT_USER, r"Environment"),
    ]:
        try:
            with winreg.OpenKey(hive, subkey) as key:
                paths.append(winreg.QueryValueEx(key, "PATH")[0])
        except FileNotFoundError:
            pass
    os.environ["PATH"] = ";".join(paths)


def setup_check() -> bool:
    """
    Point d'entrée au démarrage.
    Retourne True si tout est prêt, False si setup échoué.
    """
    if platform.system() != "Windows":
        return False  # Linux/macOS gèrent ffmpeg autrement

    deps = check_dependencies()
    if deps["ffmpeg"]:
        return True  # Tout est déjà installé

    if not deps["winget"]:
        return False

    success = install_ffmpeg()
    return success
