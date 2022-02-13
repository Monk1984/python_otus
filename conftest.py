
import requests

payload = {"box-sizing": "inherit"}
someon = requests.get("https://petstore.swagger.io/#/pet/findPetsByStatus", params=payload)

print(someon.status_code)




