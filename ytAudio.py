import os
import json
import yt_dlp
import tempfile

def runYtAudio(artist, album, cover_url, url, destdir, testing=False):
    ydl_opts = {
            'format': 'mp3/bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'test': testing,
            'postprocessors': [{  # Convert to mp3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
    }

    destination = os.path.join(destdir, artist, album)
    os.makedirs(destination, exist_ok=True)
    os.chdir(destination)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
