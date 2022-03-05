import requests
import pytest


class TestFirstApi():
    names = [
        ("X-Rate-Limit"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://petstore.swagger.io/#/user/loginUser"
        data = {'name':name}

        response = requests.get(url, params=data)
        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "string" in response_dict, "There is not field 'string' in the response."

        if len(name) == 0:
            expected_response_text = 'Hello someone'
        else:
            expected_response_text = f"Hello {name}."


        actual_response_text = response_dict["string"]
        assert actual_response_text == expected_response_text, "Нет равенства"
