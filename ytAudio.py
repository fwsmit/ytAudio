import os
import json
import yt_dlp
import tempfile
import urllib.request
import glob
import eyed3

# ℹ️ See help(yt_dlp.postprocessor.PostProcessor)
class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def __init__(self, artist, album):
        yt_dlp.postprocessor.PostProcessor.__init__(self)
        self.artist = artist
        self.album = album

    def run(self, info):
        filepath = info.get("filepath")
        audiofile = eyed3.load(filepath)
        audiofile.tag.artist = info.get("artist")
        audiofile.tag.album = info.get("album")

        # Extract the title from the filename
        audiofile.tag.title = info.get("title")
        audiofile.tag.save()
        self.to_screen('Added metadata')
        return [], info

def runYtAudio(artist, album, cover_url, url, destdir, testing=False):
    ydl_opts = {
            'format': 'mp3/bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'test': testing,
            'embed-metadata': True,
            'postprocessors': [{  # Convert to mp3
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
    }

    destination = os.path.join(destdir, artist, album)
    os.makedirs(destination, exist_ok=True)
    os.chdir(destination)
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.add_post_processor(MyCustomPP(artist, album), when='post_process')
        info = ydl.extract_info(url, download=True)

    urllib.request.urlretrieve(cover_url, "Folder.jpg")
