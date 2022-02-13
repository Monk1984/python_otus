import requests

payload = {"login":"string", "password":"string"}
respons = requests.post("https://petstore.swagger.io/#/user/loginUser", data=payload)


print(respons.text)
print(respons.status_code)
print(dict(respons.cookies))

