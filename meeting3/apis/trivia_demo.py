import json
import pprint
from http.client import HTTPResponse
from urllib.request import urlopen

trivia_url = "https://opentdb.com/api.php?amount=10&category=9&difficulty=medium&type=multiple"

response: HTTPResponse = urlopen(trivia_url)
print(type(response))
print(response.getcode())
pprint.pprint(json.loads(response.read()))