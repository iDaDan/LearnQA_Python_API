
import requests

from json_parsing import obj

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
amount = len(response.history)
last_url = response.history[amount - 2].url


# print("Редиректов:"+str(amount)+", последний урл: "+last_url)


# Скрипт для ex7: запросы и методы
def types_and_methods_test():
    response_get_no_papam = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response_get_no_papam)
    print("post, no data")

    response_get_no_param_head_test = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response_get_no_param_head_test)
    print("head, no data")

    response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                data="POST")
    print(response_get_type_post_test)
    print("post, data post")

    response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                data="DELETE")
    print(response_get_type_post_test)
    print("post, data Delete")

types_and_methods_test()