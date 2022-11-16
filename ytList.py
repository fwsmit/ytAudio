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
        artist = df['Artist'][i]
        album = df['Album'][i]
        cover_url = df['Cover URL'][i]
        url = df['URL'][i]

        runYtAudio(artist, album, cover_url, url, destdir)
