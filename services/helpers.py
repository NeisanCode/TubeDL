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

    # On accepte avc1 EN PRIORITÉ, mais on autorise VP9/AV1 en fallback
    return (
        f"bv*[height<={max_res}][vcodec^=avc1]+ba[ext=m4a]/"
        f"bv*[height<={max_res}]+ba/"  # ← fallback sans contrainte codec
        f"b[height<={max_res}]/"
        f"best"
    )


def clean_url(url):
    if not url:
        return url

    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    clean_params = {}
    if "v" in query_params:
        clean_params["v"] = query_params["v"]
    if "list" in query_params:
        clean_params["list"] = query_params["list"]
    if "si" in query_params:
        clean_params["si"] = query_params["si"]  # ← garde le paramètre si

    new_query = urlencode(clean_params, doseq=True)
    return urlunparse(parsed_url._replace(query=new_query))


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
