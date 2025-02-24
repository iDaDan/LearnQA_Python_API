import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegistered(BaseCase):
    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S") #что это?
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data)
        status_code = response.status_code
        content = response.content.decode("utf-8")

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'wjjjj@example.com'
        data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data)

        content = response.content.decode("utf-8")

        Assertions.assert_code_status(response, 400)
        assert content == f"Users with email '{email}' already exists", f"Unexpected response content"