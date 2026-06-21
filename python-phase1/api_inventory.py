import requests
import json
import logging

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    logging.info("Request successful")
    data = response.json()
    for post in data[:5]:
        print(post["title"])
        print(post["id"])
else:
    logging.error("Failed to retrieve data")

with open("posts.json", "w") as file:
    json.dump(data, file,)