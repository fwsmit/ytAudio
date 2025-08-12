#!/bin/python
import argparse as arg
from ytAudio import runYtAudio

parser = arg.ArgumentParser()
parser.add_argument('--destdir', type=str, help="Destination directory")
parser.add_argument('--list', type=str, required=True,
                    help="TXT list with youtube URL's")
args = parser.parse_args()

destdir = args.destdir
lst = args.list
with open(lst, 'r') as file:
    URLS = file.read().splitlines()

print("Checking metadata")

for url in URLS:
    if runYtAudio(url, destdir, testing=True, check_metadata=True) == -1:
        print("ERROR: url did not contain artist and album metadata: {} (nr {}) ".format(
            url, URLS.index(url)+1))
        exit(1)

answer = input("Continue downloading? (y/N): ")
if answer.lower() not in ["y", "yes"]:
    exit(0)

for url in URLS:
    runYtAudio(url, destdir, testing=False, check_metadata=False)

print("Finished downloading to", destdir)
