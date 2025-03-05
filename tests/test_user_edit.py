import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
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
        user_id_from_auth_method = self.get_json_value(response2, "user_id")

        Assertions.assert_json_value_by_name(response2, "user_id",user_id_from_auth_method,
                                             "User id from auth method is not equal to user id from check method")

        edited_data = self.prepare_registration_data()


        response3 = requests.put(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": auth_token},
                                 cookies={"auth_sid": auth_sid},
                                 data = edited_data)

        Assertions.assert_code_status(response3, 200)
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id}",
                                 headers={"x-csrf-token": auth_token},
                                 cookies= {"auth_sid": auth_sid})

        Assertions.assert_json_value_by_name(response4, "email", edited_data["email"],
                                             f"email is not edited or edited incorrectly. "
                                             f"Should be: {edited_data["email"]}. In fact {response4.json()["email"]}")