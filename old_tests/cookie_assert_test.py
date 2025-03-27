import pytest
import requests
import json

class TestCookieValue:
    def setup(self):
        self.data = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqb.ru/>]>"

    def test_cookie_value(self):
        #data = "<RequestsCookieJar[<Cookie HomeWork=hw_value for .playground.learnqb.ru/>]>"
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        resp_cookie= response.cookies
        print('RESP_COOK',resp_cookie)
        assert str(resp_cookie) == self.data, "кука приболела (cookie invalid)"
