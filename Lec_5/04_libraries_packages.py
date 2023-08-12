# packages are third party libraries
# see https://pypi.org/
# examples installed for this file: cowsay, requests
# installation: via package manager, e.g. pip

import cowsay
import sys
import requests
import json

# cowsay
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])

# requests
if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])

print(response.json()["results"][0]["trackName"])

object = response.json()
for result in object["results"]:
    print(result["trackName"])