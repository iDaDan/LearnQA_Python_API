from requests import Response
import json

class Assertions:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            # что такое assert False?
            assert False, f"response is not in JSON format. Response text is '{response.text}'"

        assert name in response_as_dict, f"response JSON doesn't have key {name}"
        assert response_as_dict[name] == expected_value, error_message