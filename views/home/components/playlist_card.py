from PIL import Image
from utils import round_corners
from .basecard import _BaseCard
from views.themes.color import *


class PlaylistCard(_BaseCard):
    """
    Carte pour un résultat de type Playlist (badge orange-rouge).

    Paramètres
    ----------
    parent   : widget parent
    title    : titre de la playlist
    quality  : qualité ex. "720P"
    duration : durée totale ex. "38:22"
    preview_image : image de vignette
    """

    def __init__(
        self,
        parent,
        title: str,
        preview_image=round_corners(Image.open("assets/images/fallback.png")),
        on_download=None,
        **kwargs,
    ):
        super().__init__(
            parent,
            title=title,
            preview_image=preview_image,
            tag_text="Playlist",
            tag_color=TAG_PLAYLIST,
            tag_fg="#FFFFFF",
            on_download=on_download,
            **kwargs,
        )
