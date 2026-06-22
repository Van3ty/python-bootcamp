import requests
import json
import logging

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:
    logging.info("Request successful")
    data = response.json()
else:
    logging.error("Failed to retrieve data")

with open("posts.json", "r") as file:
    data = json.load(file)

for post in data:
    print(post["title"])
    print(post["body"])
    print("-" * 40)