import pytest
import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("http://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "there is no user id in the response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        response2 = requests.get(
            "http://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        assert "user_id" in response2.json(), "there is no user id in the second response"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_check_method == user_id_from_auth_method, "user id from auth method not equal to user id from check method"

    #переменная exclude_params передается в test_negative_auth_check в качестве параметра,
    # это будет _параметризованный_ тест
    #чтобы не делать два одинаковых теста с отличием в одну строку
    #она добавляется не в функцию, а отдельно
    exclude_params = [
        ('no_cookie'),
        ('no_token')
    ]

    @pytest.mark.parametrize('condition', exclude_params)
    #здесь мы подключаем exclude_params
    # к ф-и test_negative_auth_check condition - это слово специальное для фреймворка или мы его сами задаём?

    def test_negative_auth_check(self, condition):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("http://playground.learnqa.ru/api/user/login", data=data)

        assert "auth_sid" in response1.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response1.headers, "There is no CSRF token header in the response"
        assert "user_id" in response1.json(), "there is no user id in the response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")

        if condition == "no_cookie":
            response2 = requests.get(
                "http://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token": token}
            )
        else:
            response2 = requests.get(
                "http://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid": auth_sid}
            )
        assert "user_id" in response2.json, "There is no user id in the second response"
        user_id_from_check_method = response2.json()["user_id"]
        assert user_id_from_check_method == 0, f"User is authorised with condition {condition}"