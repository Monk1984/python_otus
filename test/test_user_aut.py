import requests
import pytest
from lib.base_case import BaseCase

class TestUserAuth(BaseCase):

    exclud_params = [
        ("no_headers"),
        ("no cookies")
    ]

    def setup(self):
        data = {
            "username": "api-key",
            "password": "abc123"
        }

        respons1 = requests.get("http://petstore.swagger.io/v2/user/login?username=api-key&password=abc123",
                                params=data)
        self.auth_sid = self.get_cookie(respons1, "auth_sid")
        self.token = self.get_header(respons1, "x-csrf-token")
        self.user_id = self.get_json_value(respons1, "user_id")

    def test_user(self):


        respons2 = requests.get(
            "http://petstore.swagger.io/v2/user/api-key",
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid}
        )
        assert "user_id" in respons2.json(), "Ошибка ID"
        user_id_check = respons2.json()["user_id"]

        assert self.user_id == user_id_check


    @pytest.mark.parametrize('conditions',exclud_params)
    def test_negativ_auth(self, conditions):


        if conditions == "no_cookies":
            respons2 = requests.get("http://petstore.swagger.io/v2/user/login?username=api-key&password=abc123"),
            headers = {"x-csrf-token": self.token}

        else:
            respons2 = requests.get("http://petstore.swagger.io/v2/user/login?username=api-key&password=abc123"),
            cookies = {"auth_sid": self.auth_sid}

        assert "user_id" in self.respons1.json()

        user_id_check_method = respons2.json()["user_id"]

        assert user_id_check_method == 0