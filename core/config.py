import platform
from core.helpers import (
    get_ffmpeg_path,
    get_download_path,
    download_ffmpeg,
    get_node_path,
)

SYSTEM_OS = platform.system().lower()


class Config:
    download_path = get_download_path() or "./Downloads/"
    _browser_map = {
        "windows": "chrome",
        "linux": "firefox",
        "darwin": "safari",
    }
    browser_name = _browser_map.get(SYSTEM_OS, "chrome")
    ffmpeg_path = get_ffmpeg_path()
    node_path = get_node_path()
    
    if ffmpeg_path is None:
        ffmpeg_path = download_ffmpeg(SYSTEM_OS)
