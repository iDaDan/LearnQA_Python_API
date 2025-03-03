import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def edit_just_created_user(self):
        #REGISTER
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1,"id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1,"id")

        #LOGIN
        login_data = {
            "email": email,
            "password": password,
        }

        response2 = requests.post("https://playground.learnqa.ru/api/user/login", login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        auth_token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2,"user_id")

