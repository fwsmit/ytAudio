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
        cover_url = "https://upload.wikimedia.org/wikipedia/en/thumb/8/80/Wikipedia-logo-v2.svg/155px-Wikipedia-logo-v2.svg.png?20111003033239"
        url = "https://www.youtube.com/watch?v=BaW_jenozKc"
        runYtAudio(artist, album, cover_url, url, dir, testing=True)

        # test if the right files and directories exist
        destdir = os.path.join(dir, artist, album)
        self.assertTrue(os.path.isdir(destdir))
        destfile = os.path.join(destdir, "youtube-dl test video ＂'⧸⧹ä↭𝕐.mp3")
        self.assertTrue(os.path.isfile(destfile))
        
        # Remove files and test if directory is empty
        os.remove(destfile)
        self.assertFalse(os.listdir(destdir))
        os.rmdir(destdir)
        otherdir = os.path.join(dir, artist)
        os.rmdir(otherdir)
        os.rmdir(dir)

