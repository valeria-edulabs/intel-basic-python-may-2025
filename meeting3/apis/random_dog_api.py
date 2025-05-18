import json
from http.client import HTTPResponse
from urllib.request import urlopen

url = "https://random.dog/woof.json"
response: HTTPResponse = urlopen(url)
print(response)
print(response.getcode())
if response.getcode() == 200:
    data = response.read()
    print("type before load", type(data))
    data = json.loads(data)
    print("type after load", type(data))
    size = data['fileSizeBytes']
    pic_url = data['url']
    print("the size is", size, "the url", pic_url)
    pic_response = urlopen(pic_url)
    if pic_response.getcode() == 200:
        pic = pic_response.read()
        print(pic)
        ext = pic_url.split(".")[-1]
        with open(f"dog.{ext}", "wb") as f:
            f.write(pic)


