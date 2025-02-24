import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegistered(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S") #что это?
        self.email = f"{base_part}{random_part}@{domain}"
        self.data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": "wjjjj@example.com"
        }

    def test_create_user_with_existing_email(self):
        email = 'wjjjj@example.com'
        data = {
            "password":"123",
            "username":"learnqa",
            "firstName":"learnqa",
            "lastName":"learnqa",
            "email":"wjjjj@example.com"
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data)
        print(response.status_code)
        print(response.content)
        status_code = response.status_code
        content = response.content.decode("utf-8")

        assert status_code == 400, f"unexpected status code {status_code}"
        assert content == f"Users with email '{email}' already exists", f"Unexpected response content"