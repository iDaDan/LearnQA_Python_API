import json
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAgent(BaseCase):
    response_params = [
        ('no_cookie'),
        ('no_token')
    ]

    # Процесс (1) открывается. первую пару ключ-значение закидываем в реквест полностью.
    # остальные пары проверяем значения по ключам. Ну типа значение по ключу результата == значение по ключу образца.
    # ассертим, получается.
    # ну то есть, есть функция. Функция берет первую пачку пар. из пачки первую пару закидывает в реквест.
    # из образца выдираются оставшиеся ключи
    # начинается подпроцесс (2) (типа цикл) из образца  и респонса по оставшимся ключам выдираются и сравниваются значения. Если не совпали - алертим и продолжаем сравнивать
    # подпроцесс (2) заканчивается. Процесс (1) начинается со следующей первой пары ключ-значение

    def test_user_agent(self):
        params1 = [
            ('{"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Expected values":{"platform": "Mobile", "browser": "No", "device": "Android"}}'),
             ('{"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "Expected values":{"platform": "Mobile", "browser": "Chrome", "device": "iOS"}}'),
              ('{"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Expected values":{"platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}}'),
               ('{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", "Expected values":{"platform": "Web", "browser": "Chrome", "device": "No"}}'),
                ('{"User-Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "Expected values":{"platform": "Mobile", "browser": "No", "device": "iPhone"}}')
        ]

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        #


        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        print(f"params1 = {type(params1)}")
        # params1_json=json.loads(params1)
        # print(f"params1_json = {type(params1_json)}")
        # print(f"params1_json = {params1_json}")
        params1_first = params1[0]
        print(f"params1_first = {type(params1_first)}")
        print(f"params1_first = {params1_first}")
        first_params_json = json.loads(params1_first)
        print(f"first_params_json type = {type(first_params_json)}")
        print(f"first_params_json = {params1_first}")
        get_key_us_ag = first_params_json["User Agent"]
        print(f"get_key_us_ag type = {type(get_key_us_ag)}")
        print(f"get_key_us_ag = {get_key_us_ag}")
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
        print(response.text)
        response_json = json.loads(response.text)

        r_h = response.headers
        print(f"response.headers = {response.headers}")
        # for header in response.headers:
        #
        # assert response.headers ==


        my_dict = {"name": "John", "age": 30, "city": "New York", "Nice header": {"body1": "face1", "body2": "face2", "body3": "face3"}}
        print(f"my_dict = {type(my_dict)}")
        # Получаем все ключи
        nice_headers = my_dict["Nice header"]
        print(f"nice_headers = {type(nice_headers)}")
        print(f"nice_header = {nice_headers}")
        keys = nice_headers.keys()
        print(f"keys = {type(keys)}")
        print(f"keys = {keys}")
        # Преобразуем в список (если нужно)
        keys_list = list(keys)
        print(f"keys_list = {type(keys_list)}")
        print(f"keys_list = {keys_list}")

        #response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers="User Agent":)
        # Преобразуем словарь в список пар ключ-значение
        items_list = list(my_dict.items())
        # Выбираем первую пару
        print(keys)  # Вывод: dict_keys(['name', 'age', 'city'])
        print(keys_list)  # Вывод: ['name', 'age', 'city']
        #response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers="User Agent":)

        i = 0
        first_elem = params1[i]

        # print(f"first_json_str {first_json_str}")
        # json_to_list = json.loads(first_json_str)
        # print(f"json_to_list {json_to_list}")
        # first_key1, first_value1 = json_to_list[0]
        # # first_key1, first_value1 = first_json_str[0]
        # print(f"111FIST KEY AND VALUE {first_key1}, {first_value1}, FULL ITEM111 {first_json_str[0]}")
        #
        # dictator = json.loads(first_json_str)
        # # my_items = dictator.
        # keys = dictator.keys()
        # keys_list = list(keys)
        # first_user_agent = dictator["User Agent"]
        #
        # header = "User Agent"
        # header_value = "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        # response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={
        #     "User Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
        # print(response.headers)
