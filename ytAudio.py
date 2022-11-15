import os
import json
import yt_dlp
import tempfile

ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'test': False,
        'postprocessors': [{  # Conver to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
}

def runYtAudio(artist, album, cover_url, url, destdir, tempdir):
    destination = os.path.join(destdir, artist, album)
    os.makedirs(destination, exist_ok=True)
    os.chdir(destination)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
