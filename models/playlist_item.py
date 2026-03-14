from models.media import Media


class Playlist_Item(Media):
    def __init__(self, title, url, duration):
        super().__init__(title, url, duration)
        id_playlist = None
