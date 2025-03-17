import pytest

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure


class TestUserRegistered(BaseCase):

    exclude_fields = [("password"),("username"),("firstName"),("lastName"),("email")]

    def test_try_create_user_with_edited_field(self, field= None, field_value= None):
        str_field = str(field)
        data = self.prepare_registration_data()
        data[str_field] = field_value
        response = MyRequests.post("/user/", data)
        return response

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        print(data)
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
        response = self.test_try_create_user_with_edited_field(excluded_field)
        content = response.content.decode("utf-8")
        Assertions.assert_code_status(response, 400)
        assert content == f"The following required params are missed: {excluded_field}"

    @allure.description("this test try to create user with too short field that contain one character")
    @pytest.mark.parametrize("excluded_field", exclude_fields)
    def test_try_create_user_with_too_short_char_name(self, excluded_field):
        print(f"excluded_field==={excluded_field}")
        response = self.test_try_create_user_with_edited_field(excluded_field, 'a')
        content = response.content.decode("utf-8")
        Assertions.assert_code_status(response, 400)
        assert content == f"The value of '{excluded_field}' field is too short"

    @allure.description("this test try to create user with too long field that contain 250 characters")
    @pytest.mark.parametrize("excluded_field", exclude_fields)
    def test_try_create_user_with_too_long_char_name(self, excluded_field):
        print(f"excluded_field==={excluded_field}")

        field_value = ('Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
                                    'Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, '
                                    'when an unknown printer took a galley of type and scrambled it to make a type specimen book. '
                                    'It has survived not only five centuries.')
        response = self.test_try_create_user_with_edited_field(excluded_field, field_value)
        content = response.content.decode("utf-8")
        Assertions.assert_code_status(response, 400)
        assert content == f"The value of '{excluded_field}' field is too long"