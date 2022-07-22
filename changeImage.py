#!/usr/bin/env python3

from PIL import Image
import os

path = os.getenv('HOME') + '/supplier-data/images/'

for file in os.listdir(path):
    if (file.endswith('.tiff')):
        shortFileName = file.rstrip('.tiff')

        with Image.open(path + file) as im:
            im.resize((600, 400)).convert('RGB').save(path + shortFileName + ".jpeg", "JPEG")
