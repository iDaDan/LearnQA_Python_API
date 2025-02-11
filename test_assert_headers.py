import requests


def test_assert_headers():
    expected_headers_values = {'Date': 'Tue, 11 Feb 2025 09:30:36 GMT', 'Content-Type': 'application/json',
                               'Content-Length': '15',
                               'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10', 'Server': 'Apache',
                               'x-secret-homework-header': 'Some secret value', 'Cache-Control': 'max-age=0',
                               'Expires': 'Tue, 11 Feb 2025 09:30:36 GMT'}

    response = requests.get("https://playground.learnqa.ru/api/homework_header")

    #print(f"\n HEADERS: {headers}")
    response_headers = response.headers

    for key, value in expected_headers_values.items():

        assert key in response_headers, f"no {key} in response_headers"
        assert response_headers.get(key) == value, f"Значение для {key} не совпадает. Ожидаем {value}, получаем {response_headers.get(key)}"

