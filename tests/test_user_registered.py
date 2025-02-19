import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegistered(BaseCase):
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
        assert content == f"Users with email '{email}' already exists", f"Unexpected response content {content}"