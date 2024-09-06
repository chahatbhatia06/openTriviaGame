import requests
import json
from pprint import pprint


url = "https://opentdb.com/api.php?amount=50&category=11"
response = requests.get(url)
pprint(response)
pprint(response.json())
with open("trivia.json", "w") as f:
    json.dump(response.json(),f, indent=4)