import json
import requests
import os

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()
folder = "data"
os.makedirs(folder , exist_ok=True)
file_path = os.path.join(folder , "posts.json")
with open(file_path , "w" , encoding="utf-8") as fp :
    json.dump(data,fp)