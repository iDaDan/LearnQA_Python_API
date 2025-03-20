from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    def setup_method(self):
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
        self.firstname = data_create["firstName"]

        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        self.user_id_after_auth = response_create.json()["id"]

    def test_try_delete_special_authorised_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        #Login
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

        #Delete
        "https://playground.learnqa.ru/api/user/{id}"
        response_delete = MyRequests.delete("/user/2",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})

        #GET ID AFTER DELETE
        resp_get_after_delete = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            resp_get_after_delete,
            "user_id",
            2,
            f"Special User 2 is deleted"
        )



    def test_delete_authorised_user(self):
        e=2

    def test_try_delete_unauthorised_user(self):
        e=3