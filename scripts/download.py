"""Download video clip with subtitles."""
import youtube_dl


def download(link):
    ydl_opts = {
    'format': 'bestaudio/best',
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'subtitlesformat': 'vtt',
    'noplaylist': True,
    # 'skip_download': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])


if __name__ == "__main__":
    download("https://www.youtube.com/watch?v=45szHSP5xsg")