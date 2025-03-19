import json
from venv import create

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
from tests.test_user_auth import TestUserAuth


class TestUserEdit(BaseCase):

    def setup_method(self):  # так как мы перенесли данные и ассерты в специальную функцию setup_method(), то к
        # каждой содержащейся в ней переменной нужно добавить "self." слово self здесь обозначает, что переменная
        # является полем класса
        self.user_id_after_auth = None
        self.email = None
        self.password = None
        self.auth_sid = None
        self.token = None
        self.user_id_from_auth_method = None

    def create_user(self):
        # CREATE
        data_create = self.prepare_registration_data()
        self.email = data_create["email"]
        self.password = data_create["password"]

        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        self.user_id_after_auth = response_create.json()["id"]

    def test_edit_just_created_user(self):
        self.create_user()
        # LOGIN
        data = {
            'email': self.email,
            'password': self.password
        }
        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login,"auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")
        self.user_id_after_auth = self.user_id_from_auth_method

        assert "auth_sid" in response_login.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response_login.headers, "There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), "there is no user id in the response"

        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
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
            f"/user/{self.user_id_after_auth}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data=new_data
        )

        Assertions.assert_code_status(response_edit, 200)

        #GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_from_auth_method}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit != self.email, f"email {self.email} is not edited"

    def test_edit_just_created_user_invalid_email(self):
        self.create_user()
        # LOGIN
        data = {
            'email': self.email,
            'password': self.password
        }
        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")
        self.user_id_after_auth = self.user_id_from_auth_method

        assert "auth_sid" in response_login.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response_login.headers, "There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), "there is no user id in the response"

        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
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
        invalid_mail = "vjjjyashmelexmple.ru"
        invalid_mail_data = {
            "password": "123",
            "username": "learnqa",
            "firstName": "learnqa",
            "lastName": "learnqa",
            "email": invalid_mail
        }
        #Наверно можно заменить на инвалид =
        #дефолт с заменой емейл

        response_edit = MyRequests.put(
            f"/user/{self.user_id_after_auth}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data=invalid_mail_data
        )
        Assertions.assert_code_status(response_edit, 400)

        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_from_auth_method}",
                                             headers={"x-csrf-token": self.token},
                                             cookies={"auth_sid": self.auth_sid})

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit == self.email, f"email {self.email} edited to invalid mail:{email_after_edit}"

    def test_not_authorised_edit_user(self):
        self.create_user()

        new_data = self.prepare_registration_data()

        response_edit = MyRequests.put(
            f"/user/{self.user_id_after_auth}",
            data=new_data
        )
        print(f"response_edit.status_code: {response_edit.status_code}, response_edit.content: {response_edit.content}")
        Assertions.assert_code_status(response_edit, 400)

        #LOGIN
        data = {
            'email': self.email,
            'password': self.password
        }

        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")
        self.user_id_after_auth = self.user_id_from_auth_method

        assert "auth_sid" in response_login.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response_login.headers, "There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), "there is no user id in the response"

        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )



        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_after_auth}",
                                             headers={"x-csrf-token": self.token},
                                             cookies={"auth_sid": self.auth_sid})


        Assertions.assert_json_value_by_name(
            response_auth,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        print(f"response_after_edit: {response_after_edit.content}")
        email_after_edit = json.loads(response_after_edit.content)["email"]
        Assertions.assert_json_has_keys(response_after_edit, expected_fields)
        assert email_after_edit == self.email, f"email {email_after_edit} is edited without auth"