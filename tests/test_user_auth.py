import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure

@allure.epic("Authorization cases")
class TestUserAuth(BaseCase):
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    @allure.description("This test successfully request post /user/login method and preparing auth_sid, token, user_id_from_auth_method")
    def setup_method(self):  # так как мы перенесли данные и ассерты в специальную функцию setup_method(), то к
        # каждой содержащейся в ней переменной нужно добавить "self." слово self здесь обозначает, что переменная
        # является полем класса
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        with allure.step(f"вызов метода login c data {data}"):
            response1 = MyRequests.post("/user/login", data=data)

        self.auth_variables = self.get_from_response_header_cookie_json(response1,"x-csrf-token","auth_sid","user_id")

        Assertions.assert_user_login_results(response1)

        # переменная exclude_params передается в test_negative_auth_check в качестве параметра,
        # это будет _параметризованный_ тест, в который будут тянуться значения переменной благодаря
        # декоратору @pytest.mark.parametrize('condition', exclude_params)
        # чтобы не делать два одинаковых теста с отличием в одну строку
        # она добавляется не в функцию, а отдельно



    @allure.description("This test successfully authorize user by x-csrf-token and auth_sid from setup_method")
    def test_auth_user(self):
        #with allure.step("")
        self.auth_and_check(self.auth_variables)

    @allure.description("This test unsuccessfully authorize user without cookie (token or sid)")
    @pytest.mark.parametrize('condition', exclude_params)
    # здесь мы подключаем exclude_params
    # к ф-и test_negative_auth_check condition - это слово специальное для фреймворка или мы его сами задаём?
    def test_negative_auth_check(self, condition):
        if condition == "no_cookie":
            response2 = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.auth_variables["x-csrf-token"]}
            )
        else:
            response2 = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_variables["auth_sid"]}
            )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            0,
            f"User is authorised with condition {condition}"
        )
