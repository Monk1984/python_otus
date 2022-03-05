import json
import requests


json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
key = obj["messages"][0]["message"]

print(key)



payloads = requests.get("https://playground.learnqa.ru/api/long_redirect")
history = payloads.history

print(history)

data = {
            "username": "api-key",
            "password": "abc123"
        }

someon = requests.delete("https://playground.learnqa.ru/ajax/api/check_type", data)

key = data["method"][3]["method"]
print(someon.text)
print(key)




def test_my():
    phrase = input("Введите фразу короче 15 букв:")
    assert len(phrase) < 15, print("Cool!!!")



