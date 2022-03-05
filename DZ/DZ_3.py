import requests
import pytest

class TestUserAgent():

    names = [
        ( "X-Expires-Afte"),
        ("date in UTC when token expires")
    ]

    @pytest.mark.parametrize("name", names)
    def test_user_agent(self, name):
         data = {"name":name}

         url = "https://petstore.swagger.io/#/user/loginUser"


         responses = requests.get(url, params=data)
         assert "X-Expires-Afte" in responses.headers, f'Значение присутствует'
         assert responses.status_code == 200, f"Cool!!!"
