#!/bin/python
import pandas as pd
import argparse as arg
import subprocess
from ytAudio import runYtAudio

parser = arg.ArgumentParser()
parser.add_argument('--destdir', type=str, help="Destination directory")
parser.add_argument('--list', type=str, required=True, help="Excel sheet with the download info")
args = parser.parse_args()

destdir = args.destdir
list = args.list
df = pd.read_excel(list)

first=True
for i in range(len(df)):
        artist = str(df['Artist'][i])
        album = str(df['Album'][i])
        cover_url = str(df['Cover URL'][i])
        url = str(df['URL'][i])

        runYtAudio(artist, album, cover_url, url, destdir)
