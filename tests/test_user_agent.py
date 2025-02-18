import pytest
import json
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAgent(BaseCase):

    references = [
        pytest.param(json.loads('{"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "platform": "Mobile", "browser": "No", "device": "Android"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "platform": "Mobile", "browser": "Chrome", "device": "iOS"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", "platform": "Web", "browser": "Chrome", "device": "No"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "platform": "Mobile", "browser": "No", "device": "iPhone"}'))
    ]
    #def test_addition(self, data): #но какого черта тут нужен self?
    #    assert data["a"] + data["b"] == data["expected"]

    @pytest.mark.parametrize("references", references)
    def test_user_agent(self, references):
        # Используем references как словарь
        headers = {"User-Agent": references["User-Agent"]}
        print(headers)
        request = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=headers)

# Печатаем данные из ответа (если ответ содержит JSON)
        response_data = request.json()

        print(f"response = {response_data}")
        #name = ["platform", "browser", "device"]
        print(f"response_data = {type(response_data)}")
        for name in references:
            if name == "User-Agent":
                print("heh")
            else:
                print(response_data[name])


    #response = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
    #response_json = json.loads(response.text)
    #TODO До этого нужно вызвать в цикле response с нужным "User-Agent",
    # ыы
    # где-то тут нужен цикл перебора значений для, "platform", "browser", "device"}}
    # это будет значение name')

    #for User-Agent in params[0]


    #self.user_id_from_auth_method = self.get_json_value(response, "user_id")

    #print(f"params1 = {type(params1)}")
    # params1_json=json.loads(params1)
    # print(f"params1_json = {type(params1_json)}")
    # print(f"params1_json = {params1_json}")
    #params1_first = params1[0]
    #print(f"params1_first = {type(params1_first)}")
    #print(f"params1_first = {params1_first}")
    #first_params_json = json.loads(params1_first)
    #print(f"first_params_json type = {type(first_params_json)}")
    #print(f"first_params_json = {params1_first}")
    #get_key_us_ag = first_params_json["User Agent"]
    # print(f"get_key_us_ag type = {type(get_key_us_ag)}")
    # print(f"get_key_us_ag = {get_key_us_ag}")
    # response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
    # print(response.text)
    # response_json = json.loads(response.text)
    #
    # r_h = response.headers
    # print(f"response.headers = {response.headers}")
    # for header in response.headers:
    #
    # assert response.headers ==