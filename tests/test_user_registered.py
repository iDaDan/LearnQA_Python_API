import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure



class TestUserRegistered(BaseCase):

    exclude_fields = [("password"),("username"),("firstName"),("lastName"),("email")]

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

# Ex15

    @allure.description("This test unsuccessfully authorize user by email without @ symbol")
    def test_try_create_user_with_incorrect_email(self):
        email = 'wjjjjexample.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user/", data)
        content = response.content.decode("utf-8")
        print(content, "жжжь", response.status_code)
        Assertions.assert_code_status(response, 400)
        assert content == f"Invalid email format"

    @allure.description("this test try to create user with one empty field")
    @pytest.mark.parametrize("excluded_field", exclude_fields)
    def test_try_create_user_without_one_field(self, excluded_field):
        fields = self.prepare_registration_data()
        if excluded_field is not None:
            fields[excluded_field] = None
            response = MyRequests.post("/user/", fields)
            content = response.content.decode("utf-8")
            Assertions.assert_code_status(response, 400)
            assert content == f"The following required params are missed: {excluded_field}"

    @pytest.mark.parametrize("excluded_field", exclude_fields)
    def test_try_create_user_with_one_char_name(self, excluded_field):
        print(f"excluded_field==={excluded_field}")
        str_excluded_field= str(excluded_field)
        data = self.prepare_registration_data()
        data[str_excluded_field] = 'a'
        response = MyRequests.post("/user/", data)
        content = response.content.decode("utf-8")
        Assertions.assert_code_status(response, 400)
        assert content == f"The value of '{excluded_field}' field is too short"
