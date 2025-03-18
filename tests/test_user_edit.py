import json

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from tests.test_user_auth import TestUserAuth


class TestUserEdit(BaseCase):

    def setup_method(self):  # так как мы перенесли данные и ассерты в специальную функцию setup_method(), то к
        # каждой содержащейся в ней переменной нужно добавить "self." слово self здесь обозначает, что переменная
        # является полем класса
        # CREATE
        data_before = self.prepare_registration_data()
        self.email = data_before["email"]
        self.password = data_before["password"]
        print(f"data_before: {data_before}, email: {self.email}")
        response_create = MyRequests.post(
            "/user/",
            data_before
        )
        print(response_create)

        self.auth_sid = self.get_cookie(response_create,"auth_sid")
        self.token = self.get_header(response_create, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_create, "user_id")

        assert "auth_sid" in response_create.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response_create.headers, "There is no CSRF token header in the response"
        assert "user_id" in response_create.json(), "there is no user id in the response"



    def test_edit_just_created_user(self):

        # LOGIN
        data = {
            'email': self.email,
            'password': self.password
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1,"auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

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
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        # GET DATA BEFORE EDIT
        # лежит в  data_before

        # EDIT
        new_data = self.prepare_registration_data()
        response_edit = MyRequests.put(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data=new_data
        )

        Assertions.assert_code_status(response_edit, 200)

        #GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_from_auth_method}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit != self.email, f"email {email} is not edited"


    def test_not_authorised_edit_user(self):

        # GET DATA BEFORE EDIT
        # лежит в  data_before

        # EDIT
        new_data = self.prepare_registration_data()
        print(self.user_id_from_auth_method)
        response_edit = MyRequests.put(
            f"/user/{self.user_id_from_auth_method}",
            data=new_data
        )

        Assertions.assert_code_status(response_edit, 200)

        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_from_auth_method}",
                                             headers={"x-csrf-token": token},
                                             cookies={"auth_sid": auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit != email, f"email {email} is not edited"