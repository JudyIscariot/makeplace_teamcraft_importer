## Imports a file from a directory and loads the json from it into memory.
## The json is then posted to a url in teamcraft

## Usage: python makeplace_importer.py
## Example: python makeplace_importer.py
import json
from pkgutil import iter_importers
from unicodedata import name
import requests
import sys
import os
import time
import base64

thefile = input("Enter the file to import: ")

data = open(thefile, "r")
json_data = json.load(data)

interiorFixtures = json_data["interiorFixture"]
exteriorFixtures = json_data["exteriorFixture"]
interiorFurniture = json_data["interiorFurniture"]
exteriorFurniture = json_data["exteriorFurniture"]

furniturelist = []

for item in interiorFixtures:
    furniturelist.append(item["itemId"])
for item in exteriorFixtures:
    furniturelist.append(item["itemId"])
for item in interiorFurniture:
    furniturelist.append(item["itemId"])
    for attachment in item["attachments"]:
        furniturelist.append(attachment["itemId"])
for item in exteriorFurniture:
    furniturelist.append(item["itemId"])
    for attachment in item["attachments"]:
        furniturelist.append(attachment["itemId"])

finalList = {0:1}
for item in furniturelist:
    if item in finalList:
        finalList[item] += 1
    else:
        finalList[item] = 1
    
url = "https://ffxivteamcraft.com/import/"

del finalList[0]

encodablestring = ""
for item in finalList:
    encodablestring += str(item) + ",null," + str(finalList[item]) + ";"
encodeable = encodablestring[:-1]

finalstring = base64.b64encode(encodeable.encode('utf-8'))
print(url+finalstring.decode('utf-8'))

