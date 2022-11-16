import unittest
import os
import shutil
from tempfile import mkdtemp
from ytAudio import runYtAudio

class TestAudio(unittest.TestCase):

    def testAudio(self):
        dir = mkdtemp()
        print(dir)
        artist = "a"
        album = "b"
        cover_url = "https://www.sample-videos.com/img/Sample-jpg-image-50kb.jpg"
        url = "https://www.youtube.com/watch?v=BaW_jenozKc"
        runYtAudio(artist, album, cover_url, url, dir, testing=True)

        # test if the right files and directories exist
        destdir = os.path.join(dir, artist, album)
        self.assertTrue(os.path.isdir(destdir))
        destfile = os.path.join(destdir, "youtube-dl test video ＂'⧸⧹ä↭𝕐.mp3")
        self.assertTrue(os.path.isfile(destfile))
        cover = os.path.join(destdir, "Folder.jpg")
        self.assertTrue(os.path.isfile(cover))
        
        remove = False
        # Remove files and test if directory is empty
        if remove:
            os.remove(destfile)
            os.remove(cover)
            self.assertFalse(os.listdir(destdir))
            os.rmdir(destdir)
            otherdir = os.path.join(dir, artist)
            os.rmdir(otherdir)
            os.rmdir(dir)

