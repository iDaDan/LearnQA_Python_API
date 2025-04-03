import allure
from requests import Response
import json

class Assertions:
    @staticmethod
    @allure.description(f"Asserting json value with expected")
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"

        with allure.step(f"using vars: response_as_dict[name]: "
                         f"{response_as_dict[name]}, expected_value: {expected_value}"):
            assert name in response_as_dict, f"response JSON doesn't have key {name}"
            assert response_as_dict[name] == expected_value, error_message

    @staticmethod
    @allure.description(f"Asserting: json value not equal to expected")
    def assert_json_unequal_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f"using vars: response_as_dict[name]: "
                        f"{response_as_dict[name]}, expected_value: {expected_value}"):
            assert name in response_as_dict, f"response JSON doesn't have key {name}"
            assert response_as_dict[name] != expected_value, error_message

    @staticmethod
    @allure.description(f"Asserting: json has key")
    def assert_json_has_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"
        with allure.step(f"using vars: response_as_dict[name]: "
                         f"{response_as_dict[name]}"):
            assert name in response_as_dict, f"response JSON doesn't have key {name}"

    @staticmethod
    @allure.description(f"Asserting: json has keys")
    def assert_json_has_keys(response: Response, names:list):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"
        for name in names:
            assert name in response_as_dict, f"response JSON doesn't have key {name}"

    @staticmethod
    @allure.description(f"Asserting: json has no key")
    def assert_json_has_no_key(response: Response, name):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"

        assert name not in response_as_dict, f"response JSON has unexpected key {name}"

    @staticmethod
    @allure.description(f"Asserting: code status")
    def assert_code_status(response: Response, expected_status_code):
        #почему не применяем тут try except?
        assert response.status_code == expected_status_code, \
            f"unexpected status code. Expected {expected_status_code}, Actual {response.status_code}"

    @staticmethod
    @allure.description(f"Asserting results of user login")
    def assert_user_login_results(response: Response):
        assert "auth_sid" in response.cookies, "there is no auth cookie in response"
        assert "x-csrf-token" in response.headers, "There is no CSRF token header in the response"
        assert "user_id" in response.json(), "there is no user id in the response"

