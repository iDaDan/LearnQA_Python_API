import requests

def test_assert_headers():
    response = requests.get("https://playground.learnqa.ru/api/homework_header")
    headers = response.headers
    response_as_dict = response.json()
    print(f"{headers}, {response_as_dict}")