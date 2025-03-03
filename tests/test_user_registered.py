import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegistered(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'wjjjj@example.com'
        data = self.prepare_registration_data(email)

        response = requests.post("https://playground.learnqa.ru/api/user/", data)
        content = response.content.decode("utf-8")

        Assertions.assert_code_status(response, 400)
        assert content == f"Users with email '{email}' already exists", f"Unexpected response content"