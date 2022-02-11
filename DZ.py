import json
import requests


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
key = obj["messages"][0]["message"]

print(key)



payloads = requests.get("https://playground.learnqa.ru/api/long_redirect")
history = payloads.history

print(history)