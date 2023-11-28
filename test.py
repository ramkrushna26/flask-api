import requests

BASE = "http://127.0.0.1:5000/"

#responce = requests.put(BASE + "video/1", {"name": "ramk", "likes": 10})
#print(responce.json())
#input()
responce = requests.get(BASE + "video/4")
print(responce.json())