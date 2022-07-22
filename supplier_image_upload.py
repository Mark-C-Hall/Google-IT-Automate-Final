#!/usr/bin/env python3

import requests
import os

path = os.getenv('HOME') + '/supplier-data/images/'
url = "http://localhost/upload/"

for file in os.listdir(path):
    if (file.endswith('.jpeg')):
        with open(path + file, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
