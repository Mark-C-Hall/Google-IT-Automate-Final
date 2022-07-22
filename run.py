#! /usr/bin/env python3

import os
import requests

path = os.getenv('HOME') + '/supplier-data/descriptions/'
url = "http://localhost/fruits/"

for file in os.listdir(path):
    data = {}
    imageName = file.replace('txt', 'jpeg')
    data["image_name"] = imageName
    with open(path + file) as f:
        name = f.readline().rstrip()
        weight = int(f.readline().rstrip(' lbs\n'))
        description = f.read()

        data["name"] = name
        data["weight"] = weight
        data["description"] = description

    r = requests.post(url, json=data)
