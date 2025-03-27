import allure
import pytest
import json
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserAgent(BaseCase):

    references = [
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "platform": "Mobile", "browser": "Chrome", "device": "iOS"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "platform": "Googlebot", "browser": "Unknown", "device": "Unknown"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", "platform": "Web", "browser": "Chrome", "device": "No"}')),
        pytest.param(json.loads('{"User-Agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "platform": "Mobile", "browser": "No", "device": "iPhone"}'))
    ]
    #def test_addition(self, data): #но какого черта тут нужен self?
    #    assert data["a"] + data["b"] == data["expected"]
    @allure.description("This test successfully check consistency of User-Agent value")
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
                user_agent = references[name]
            else:
                assert response_data[name] == references[name], f"Для User-Agent {user_agent} Значения {name} не равны. Контрольное: {references[name]}, фактическое: {response_data[name]}"
