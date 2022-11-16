import unittest
import os
import shutil
from tempfile import mkdtemp
from ytAudio import runYtAudio
import eyed3

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

    def testAudio2(self):
        dir = mkdtemp()
        print(dir)
        artist = "Froukje"
        album = "Licht En Donker"
        cover_url = "https://lh3.googleusercontent.com/17FgrLz89EJYLZQyH1WdEeOYu0VuJedeaQF_BghApwwAr5tEloLbdTFlsEZYWYXX0avC3Esc9PedkwU=w544-h544-l90-rj"
        url = "https://music.youtube.com/playlist?list=OLAK5uy_nklMWkxEJReWtIy_AiNrlNUM6eVL2_ycs"
        runYtAudio(artist, album, cover_url, url, dir, testing=True)

        # test if the right files and directories exist
        destdir = os.path.join(dir, artist, album)
        self.assertTrue(os.path.isdir(destdir))
        song1 = os.path.join(destdir, "Licht En Donker.mp3")
        song2 = os.path.join(destdir, "Heb Ik Dat Gezegd？.mp3")
        song3 = os.path.join(destdir, "Ik Wil Dansen.mp3")
        song4 = os.path.join(destdir, "Goud.mp3")
        song5 = os.path.join(destdir, "17.mp3")
        song6 = os.path.join(destdir, "Onbezonnen.mp3")
        self.assertTrue(os.path.isfile(song1))
        self.assertTrue(os.path.isfile(song2))
        self.assertTrue(os.path.isfile(song3))
        self.assertTrue(os.path.isfile(song4))
        self.assertTrue(os.path.isfile(song5))
        self.assertTrue(os.path.isfile(song6))
        cover = os.path.join(destdir, "Folder.jpg")
        self.assertTrue(os.path.isfile(cover))

        audiofile = eyed3.load(song2)
        self.assertEqual(audiofile.tag.artist, "Froukje")
        self.assertEqual(audiofile.tag.title, "Heb Ik Dat Gezegd?")
        self.assertEqual(audiofile.tag.album, "Licht En Donker")

        remove = False
        # Remove files and test if directory is empty
        if remove:
            # TODO remove files
            os.remove(cover)
            self.assertFalse(os.listdir(destdir))
            os.rmdir(destdir)
            otherdir = os.path.join(dir, artist)
            os.rmdir(otherdir)
            os.rmdir(dir)
