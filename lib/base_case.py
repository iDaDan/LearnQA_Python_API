import json.decoder
from requests import Response
from datetime import datetime
from lib.assertions import Assertions
import allure
from lib.my_requests import MyRequests


class BaseCase:
    # BaseCase - это наше самостоятельное название файла или часть pytest или другой библиотеки?
    def get_cookie(self, response: Response, cookie_name): # response: Response - это что?
        assert cookie_name in response.cookies, f"Cannot find cookie with name {cookie_name} in the last response"
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"Cannot find headers with name {headers_name} in the last response"
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError: #мы делаем это, чтобы получить тип ошибки менно из модуля JSONDecodeError?
            assert False, f"response is not in the JSON format. The response text is '{response.text}'"

        assert name in response_as_dict, f"response doesn't have key '{name}'"
        return response_as_dict[name]

    def prepare_registration_data(self, email=None):
        with allure.step(f"data creation with email: {email}"):
            if email is None:
                base_part = "learnqa"
                domain = "example.com"
                random_part = datetime.now().strftime("%m%d%Y%H%M%S") #что это?
                email = f"{base_part}{random_part}@{domain}"
            default_data = {
                "password": "123",
                "username": "learnqa",
                "firstName": "learnqa",
                "lastName": "learnqa",
                "email": email
            }
            return default_data

    def create_user_and_check(self, email=None, **kwargs):
        # CREATE
        data_create = self.prepare_registration_data(email)
        email = data_create["email"]
        password = data_create["password"]
        firstname = data_create["firstName"]
        username = data_create["username"]
        lastname = data_create["lastName"]

        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        user_id_after_create = response_create.json()["id"]

        data = {
            'email': email,
            'password': password
        }
        response_login = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_header(response_login, "x-csrf-token")
        user_id_after_check = self.get_json_value(response_login, "user_id")

        assert "auth_sid" in response_login.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response_login.headers, "There is no CSRF token header in the response"
        assert "user_id" in response_login.json(), "there is no user id in the response"

        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response_auth,
            "user_id",
            user_id_after_check,
            "User id from auth method is not equal to user id from check method"
        )
        return {"auth_sid":auth_sid,
                "password":password,
                "token":token,
                "user_id_after_create":user_id_after_create,
                "user_id_after_check": user_id_after_check,
                "email": email,
                "firstName":firstname,
                "username":username,
                "lastname":lastname
                }

    def create_user_and_check_auth(self, email=None, **kwargs):
        # CREATE
        data_create = self.prepare_registration_data()
        for jopa in data_create:
            self.jopa = data_create[f"{jopa}"]
        # self.email = data_create["email"]
        # self.password = data_create["password"]
        # self.firstname = data_create["firstName"]

        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        self.user_id_after_auth = response_create.json()["id"]