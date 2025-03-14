from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure
from environment import ENV_OBJECT

class TestUserRegistered(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'wjjjj@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data)
        content = response.content.decode("utf-8")

        Assertions.assert_code_status(response, 400)
        assert content == f"Users with email '{email}' already exists", f"Unexpected response content"

    @allure.description("This test unsuccessfully authorize user by email without @ symbol")
    def test_try_create_user_with_incorrect_email(self):
        email = 'wjjjjexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data)
        content = response.content.decode("utf-8")
        print(content, "жжжь", response.status_code)