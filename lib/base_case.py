import json.decoder
from requests import Response
from datetime import datetime

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

    def prepare_registration_data(self, email=None, **kwargs):
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
        default_data.update(kwargs)
        return default_data