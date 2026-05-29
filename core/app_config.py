from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    APP_NAME: str = "TubeDL"
    VERSION: str = "1.0.0"
    FFMPEG_BINARY_DIR: str = ""
    
