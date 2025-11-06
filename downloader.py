import yt_dlp
import yt_dlp.utils


def downloader(
    url, media_type, media_path, cookie_path, ffmpeg_path, progress_hook: callable
):
    ydl_opts = {
        "cookies": cookie_path,
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ffmpeg_location": ffmpeg_path,
        "quiet": False,
        "progress_hooks": [lambda d: progress_hook(d)],
    }

    if media_type.lower() == "video":
        ydl_opts["outtmpl"] = f"{media_path}/%(title)s.%(ext)s"
        ydl_opts["noplaylist"] = True
    elif media_type.lower() == "playlist":
        ydl_opts["outtmpl"] = (
            f"{media_path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s"
        )
        ydl_opts["noplaylist"] = False

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except yt_dlp.utils.DownloadError as e:
        raise
    except Exception as e:
        raise
