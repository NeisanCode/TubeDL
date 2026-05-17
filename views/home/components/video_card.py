from .basecard import _BaseCard
from views.themes.color import *
from PIL import Image
from utils import round_corners


class VideoCard(_BaseCard):
    """
    Carte pour un résultat de type Vidéo (badge jaune).

    Paramètres
    ----------
    parent   : widget parent
    title    : titre de la vidéo
    quality  : qualité ex. "720P"
    duration : durée  ex. "3:33"
    preview_image : image de vignette
    """

    def __init__(
        self,
        parent,
        title: str,
        quality: str = "720P",
        duration: str = "0:00",
        queue=None,
        preview_image=round_corners(Image.open("assets/images/fallback.png")),
        on_download=None,
        **kwargs,
    ):
        super().__init__(
            parent,
            title=title,
            quality=quality,
            duration=duration,
            queue=queue,
            on_download=on_download,
            tag_text="Video",
            tag_color=TAG_VIDEO,
            tag_fg="#111111",
            preview_image=preview_image,
            **kwargs,
        )
