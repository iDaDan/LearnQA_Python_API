import json

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from tests.test_user_auth import TestUserAuth


class TestUserEdit(BaseCase):

    # def setup_method(self):  # так как мы перенесли данные и ассерты в специальную функцию setup_method(), то к
    #     # каждой содержащейся в ней переменной нужно добавить "self." слово self здесь обозначает, что переменная
    #     # является полем класса
    #     data = {
    #         'email': 'vinkotov@example.com',
    #         'password': '1234'
    #     }
    #     response1 = MyRequests.post("/user/login", data=data)
    #
    #     self.auth_sid = self.get_cookie(response1,"auth_sid")
    #     self.token = self.get_header(response1, "x-csrf-token")
    #     self.user_id_from_auth_method = self.get_json_value(response1, "user_id")
    #
    #     assert "auth_sid" in response1.cookies, "there is no auth cookie in response"
    #     assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
    #     assert "user_id" in response1.json(), "there is no user id in the response"

    def test_edit_just_created_user(self):
        # CREATE
        data_before = self.prepare_registration_data()
        email = data_before["email"]
        password = data_before["password"]
        print(f"data_before: {data_before}, email: {email}")
        response_create = MyRequests.post(
            "/user/",
            data_before
        )
        print(response_create)

        # LOGIN
        data = {
            'email': email,
            'password': password
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1,"auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        assert "auth_sid" in response1.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "there is no user id in the response"

        #
        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response_auth,
            "user_id",
            user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        # GET DATA BEFORE EDIT
        # лежит в  data_before

        # EDIT
        new_data = self.prepare_registration_data()
        response_edit = MyRequests.put(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=new_data
        )

        Assertions.assert_code_status(response_edit, 200)

        #GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit != email, f"email {email} is not edited"


    def test_not_authorised_edit_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        edited_data = self.prepare_registration_data()

        # EDIT
        response3 = MyRequests.put(f"/user/{user_id}",
                                   data=edited_data)
        Assertions.assert_code_status(response3, 400)
        response4 = MyRequests.get(f"/user/{user_id}")

        # LOGIN
        login_data = {
            "email": email,
            "password": password,
        }

        response2 = MyRequests.post("/user/login", login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        auth_token = self.get_header(response2, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response2, "user_id")
        Assertions.assert_json_value_by_name(response2, "user_id", user_id_from_auth_method,
                                             "User id from auth method is not equal to user id from check method")

        # CHECK
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": auth_token},
                                   cookies={"auth_sid": auth_sid})
        Assertions.assert_json_unequal_value_by_name(response4, "email", edited_data["email"],
                                             f"email is not edited or edited incorrectly. "
                                             f"Should be: {edited_data["email"]}. In fact {response4.json()["email"]}")
