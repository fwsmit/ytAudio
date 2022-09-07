import pandas as pd
import argparse as arg
import subprocess

parser = arg.ArgumentParser()
parser.add_argument('--tmpdir', type=str, help="Temporary directory to use")
parser.add_argument('--destdir', type=str, help="Destination directory")
args = parser.parse_args()
df = pd.read_excel('TestList.xlsx')

def runYtAudio(artist, album, cover_url, url, destdir, tempdir):
    command_line = ["./ytAudio", "-a", artist, "-A", album, "-c", cover_url]
    if destdir:
        command_line.extend(["-d", destdir])

    if tempdir:
        command_line.extend(["-t", tempdir])

    command_line.append(url)
    print(command_line)
    subprocess.run(command_line)

destdir = args.destdir
tmpdir = args.tmpdir

first=True
for i in range(len(df)):
        artist = df['Artist'][i]
        album = df['Album'][i]
        cover_url = df['Cover URL'][i]
        url = df['URL'][i]

        runYtAudio(artist, album, cover_url, url, destdir, tmpdir)
