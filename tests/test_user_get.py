import json

import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests


class TestUserGet(BaseCase):

    @allure.description("This test getting data about not auth-ed user")
    @allure.tag("get", "crit")
    def test_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_no_key(response, "email")
        Assertions.assert_json_has_no_key(response, "firstName")
        Assertions.assert_json_has_no_key(response, "lastname")

    @allure.description("This test getting data about auth-ed user")
    @allure.tag("get", "user", "crit", "positive", "smoke")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_var = self.get_from_response_header_cookie_json(
            response1,
            "x-csrf-token",
            "auth_sid",
            "user_id"
        )

        response2 = MyRequests.get(f"/user/{auth_var["user_id"]}",
                                 headers={"x-csrf-token": auth_var["x-csrf-token"]},
                                 cookies= {"auth_sid": auth_var["auth_sid"]})

        expected_fields = ["username","email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("This test try to get data about other user")
    @allure.tag("get", "user", "crit")
    def test_get_user_details_auth_as_another_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_var = self.get_from_response_header_cookie_json(
            response1,
            "x-csrf-token",
            "auth_sid",
            "user_id"
        )

        response2 = MyRequests.get(f"/user/3",
                                 headers={"x-csrf-token": auth_var["x-csrf-token"]},
                                 cookies= {"auth_sid": auth_var["auth_sid"]})

        Assertions.assert_json_has_key(response2,"username")
        unexpected_keys = {}
        if len(response2.json()) > 1:
            for key in response2:
                unexpected_keys[key] = [key]
            assert False, f"response has unexpected key(s) {unexpected_keys}"