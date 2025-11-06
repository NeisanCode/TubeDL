import yt_dlp


def downloader(url, media_type, media_path, progress_hook: callable):
    ydl_opts = {
        "cookies": "cookies.txt",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "ffmpeg_location": "/usr/bin/ffmpeg",
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
        print("Download completed!")
    except Exception as e:
        print(f"Download failed: {e}")
