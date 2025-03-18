from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):

    def setup_method(self):  # так как мы перенесли данные и ассерты в специальную функцию setup_method(), то к
        # каждой содержащейся в ней переменной нужно добавить "self." слово self здесь обозначает, что переменная
        # является полем класса
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response1,"auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        assert "auth_sid" in response1.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "there is no user id in the response"

    def test_try_delete_special_authorised_user(self):

        response2 = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},  # как и почему тут self?
            cookies={"auth_sid": self.auth_sid}
        )


        response3 = MyRequests.delete("/user/2", self.data)
        print(response2.text, " _sc_ ", response2.status_code)

        response = MyRequests.delete(
            "/user/2",
            headers={"x-csrf-token": self.token},  # как и почему тут self?
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

    def test_delete_authorised_user(self):
        e=2

    def test_try_delete_unauthorised_user(self):
        e=3