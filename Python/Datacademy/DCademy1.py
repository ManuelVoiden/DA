#Nueva versión del conversor de monedas

import math
import json
import requests

from pprint import pprint

apiFile= open("api.json")

data.json.load(apiFile)
api_key=data["API_KEY"]

url="http://data.fixer.io/api/latest" +api_key

dataURL= requests.get(url).text
dataJSON= json.loads(dataURL)

