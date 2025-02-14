import json
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserAgent:

    def test_jopa_govna(self):
        my_dict = {"name": "John", "age": 30, "city": "New York"}

        # Получаем все ключи
        keys = my_dict.keys()

        # Преобразуем в список (если нужно)
        keys_list = list(keys)

        print(keys)  # Вывод: dict_keys(['name', 'age', 'city'])
        print(keys_list)  # Вывод: ['name', 'age', 'city']
        params = '{"values":[{"User Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","platform": "Mobile", "browser": "No", "device": "Android"},{"User Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "Chrome", "device": "iOS"}, {"User Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}, {"User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0","platform": "Web", "browser": "Chrome", "device": "No"},{"User Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "No", "device": "iPhone"}]}'
        #response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers=)
        params1 = ('{"User Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","platform": "Mobile", "browser": "No", "device": "Android"}'),('{"User Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "Chrome", "device": "iOS"}'), ('{"User Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}'), ('{"User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0","platform": "Web", "browser": "Chrome", "device": "No"}'),('{"User Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "No", "device": "iPhone"}')

        params1 = (
            '{"User Agent":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30","platform": "Mobile", "browser": "No", "device": "Android"}',
            '{"User Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "Chrome", "device": "iOS"}',
            '{"User Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}',
            '{"User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0","platform": "Web", "browser": "Chrome", "device": "No"}',
            '{"User Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1","platform": "Mobile", "browser": "No", "device": "iPhone"}'
        )

        first_json_str = params1[0]
        first_dict = json.loads(first_json_str)
        keys = first_dict.keys()
        keys_list = list(keys)

        # Процесс (1) открывается. первую пару ключ-значение закидываем в реквест полностью.
        # остальные пары проверяем значения по ключам. Ну типа значение по ключу результата == значение по ключу образца.
        # ассертим, получается.
        # ну то есть, есть функция. Функция берет первую пачку пар. из пачки первую пару закидывает в реквест.
        # из образца выдираются оставшиеся ключи
        # начинается подпроцесс (2) (типа цикл) из образца  и респонса по оставшимся ключам выдираются и сравниваются значения. Если не совпали - алертим и продолжаем сравнивать
        # подпроцесс (2) заканчивается. Процесс (1) начинается со следующей первой пары ключ-значение

        first_user_agent = first_dict["User Agent"]

        header = "User Agent"
        header_value = "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"})
        print(response.headers)
