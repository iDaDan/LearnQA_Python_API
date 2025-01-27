import pytest
import requests
import json

class TestCookieValue:
    def setup(self):
        data = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqb.ru/>]>"

    def test_cookie_value(self):
        value = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqb.ru/>]>"
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        resp_cookie= response.cookies
        print(resp_cookie)
        assert str(resp_cookie) == value, "кука приболела (cookie invalid)"
