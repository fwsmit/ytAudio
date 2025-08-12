import os
import yt_dlp
import urllib.request
import eyed3

# ℹ️ See help(yt_dlp.postprocessor.PostProcessor)


class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def __init__(self):
        yt_dlp.postprocessor.PostProcessor.__init__(self)

    def run(self, info):
        filepath = info.get("filepath")
        audiofile = eyed3.load(filepath)
        audiofile.tag.artist = info.get("artist")
        audiofile.tag.album = info.get("album")
        audiofile.tag.track_num = (
            info.get("playlist_autonumber"), info.get("n_entries"))
        release_year = info.get("release_year")
        if release_year:
            audiofile.tag.recording_date = eyed3.core.Date(release_year)

        audiofile.tag.title = info.get("title")
        audiofile.tag.save()
        self.to_screen(
            'Processed {} - {}'.format(audiofile.tag.artist, audiofile.tag.title))
        return [], info


def get_artist(info):
    a = info.get("artist")
    if a:
        return a
    else:
        return info.get("entries")[0].get("artist")


def get_album(info):
    a = info.get("album")
    if a:
        return a
    else:
        return info.get("entries")[0].get("album")


def runYtAudio(url, destdir, testing=False, check_metadata=False):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'outtmpl': '%(artist,channel)s/%(album,playlist_title)s/%(title)s.%(ext)s',
        'test': testing,
        'embed-metadata': True,
        'quiet': True,
        'postprocessors': [{  # Convert to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    # destination = os.path.join(destdir, artist, album)
    os.makedirs(destdir, exist_ok=True)
    os.chdir(destdir)

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        if check_metadata:
            info = ydl.extract_info(url, download=False)
            if not get_artist(info):
                print("Could not find artist for: ",
                      info.get("title"), "(", url, ")")
                print(info['album'])
                return -1

            if not get_album(info):
                print("Could not find album for: ",
                      info.get("title"), "(", url, ")")
                return -1
            else:
                print("Info: {} - {}".format(get_artist(info), get_album(info)))
        else:
            ydl.add_post_processor(MyCustomPP(), when='post_process')
            _ = ydl.extract_info(url, download=True)

    # urllib.request.urlretrieve(cover_url, "Folder.jpg")
