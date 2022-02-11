from json.decoder import JSONDecodeError
import requests

response = requests.get("https://petstore.swagger.io/#/pet/findPetsByStatus/", params={"available": "pending"})
print(response.text)

try:
    parsed_respons_text = response.json()
    print(parsed_respons_text)
except JSONDecodeError:
    print("Respons is not JSON format")