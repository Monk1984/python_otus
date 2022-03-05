import requests


def test_headers():

    respons = requests.get("https://playground.learnqa.ru/api/homework_header")
    print(respons.headers)

    assert respons.headers == "homework"