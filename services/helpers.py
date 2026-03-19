from urllib.parse import urlencode, urlparse, parse_qs, urlunparse


def get_format_selector(res: str) -> str:
    match res:
        case "2160p" | "4k":
            return "bv*[height<=2160]+ba/bv*[height<=1440]+ba/bv*[height<=1080]+ba/bv*[height<=720]+ba/bv*[height<=480]+ba/bv*[height<=360]+ba/b"

        case "1440p":
            return "bv*[height<=1440]+ba/bv*[height<=1080]+ba/bv*[height<=720]+ba/bv*[height<=480]+ba/bv*[height<=360]+ba/b"

        case "1080p":
            return "bv*[height<=1080]+ba/bv*[height<=720]+ba/bv*[height<=480]+ba/bv*[height<=360]+ba/b"

        case "720p":
            return "bv*[height<=720]+ba/bv*[height<=480]+ba/bv*[height<=360]+ba/b"

        case "480p":
            return "bv*[height<=480]+ba/bv*[height<=360]+ba/b"

        case "360p":
            return "bv*[height<=360]+ba/b"

        case _:
            return "bv*+ba/b"  # fallback total (meilleure qualité)


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