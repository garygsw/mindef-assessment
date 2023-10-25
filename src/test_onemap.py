import json

import requests

url = "https://www.onemap.gov.sg/api/common/elastic/search?searchVal=%s&returnGeom=Y&getAddrDetails=Y&pageNum=1"

headers = {'Authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIwMWM0Zjc4MjExZDYwMzMyNjUwY2FjMWMzYTc1ODM5NSIsImlzcyI6Imh0dHA6Ly9pbnRlcm5hbC1hbGItb20tcHJkZXppdC1pdC0xMjIzNjk4OTkyLmFwLXNvdXRoZWFzdC0xLmVsYi5hbWF6b25hd3MuY29tL2FwaS92Mi91c2VyL3Bhc3N3b3JkIiwiaWF0IjoxNjk4MjAwMTc1LCJleHAiOjE2OTg0NTkzNzUsIm5iZiI6MTY5ODIwMDE3NSwianRpIjoicFpzUXVsYzNuc3BqNEx2RCIsInVzZXJfaWQiOjEzODAsImZvcmV2ZXIiOmZhbHNlfQ.by5nE2Q3UX08tqlIqDNHXK3sMPtBmzdCzj3BubX0f7Q'}

response = requests.request("GET", url % "674A YISHUN AVE 4", headers=headers)
results = json.loads(response.text)
print(results["results"][0])
