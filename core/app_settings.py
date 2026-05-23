from dataclasses import dataclass
from .helpers_settings import HelperSettings


# @dataclass(frozen=True)
class UserSettings:
    DOWNLOAD_FOLDER: str = HelperSettings.load_download_folder()
    COOKIES_PATH: str = HelperSettings.load_cookie_file()
    DEFAULT_THEME: str = HelperSettings.load_default_theme()
