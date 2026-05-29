from urllib.parse import urlencode, urlparse, parse_qs, urlunparse
from core import AppSettings


def get_format_selector(res: str):
    quality_map = {
        "4k": 2160,
        "2160p": 2160,
        "1440p": 1440,
        "1080p": 1080,
        "720p": 720,
        "480p": 480,
        "360p": 360,
    }

    max_res = quality_map.get(res, 1080)

    return f"bv*[height<={max_res}][vcodec^=avc1]+ba/" f"b[height<={max_res}]/" f"best"


def clean_youtube_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params.pop("list", None)
    new_query = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query))
    return new_url


def clean_url(url):
    # On vérifie si c'est une URL courte avec une playlist
    if "youtu.be/" in url and "?list=" in url:
        # 1. On sépare la base des paramètres
        # Exemple: ["https://youtu.be/Z2zD3EdjpNo", "list=PLKm..."]
        parties = url.split("?")
        url_base_avec_id = parties[0]

        # L'url_base_avec_id contient déjà "https://youtu.be/ID_VIDEO"
        # On retourne simplement cette partie
        return url_base_avec_id
    return url


def format_duration(seconds):
    if not seconds:
        return "0:00"
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)

    if h:
        return f"{h}:{m:02}:{s:02}"
    return f"{m}:{s:02}"


def load_cookie():
    cookie_file = AppSettings.load_cookie_file()[0]
    cookie_config = (
        {f"cookiefile": cookie_file}
        if cookie_file
        else {"cookiefrombrowser": ("chrome",)}
    )
    return cookie_config
