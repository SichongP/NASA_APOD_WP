#!/usr/bin/env python3

import requests, datetime, urllib, pathlib, os

img_folder = str(pathlib.Path.home()) + "/NASA_APOD/"
if not os.path.exists(img_folder):
    os.makedirs(img_folder)
date = str(datetime.datetime.date(datetime.datetime.today()))
if os.path.exists(os.path.join(img_folder, date + ".jpg")):
    exit(0)
metadata = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
print(metadata.json()['explanation'])
file_path, header = urllib.request.urlretrieve(metadata.json()['hdurl'], img_folder + date + ".jpg")
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file://" + file_path)


