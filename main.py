from gettext import gettext

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

def all_types_and_methods_test():
    method_type = ["get", "post", "put", "delete"]
    data = ["GET", "POST", "PUT", "DELETE"]

    data_type_number = 1
    # рабочая конкретная строка:
    #print(requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST"))
    #method_name in method_type:
    method_type = ["get", "post", "put", "delete"]
    method_type_number = 1
    while method_type_number < 4:
        method = getattr(requests, method_type[method_type_number])
        data = ["GET", "POST", "PUT", "DELETE"]
        data_type_number = 1
        while data_type_number < 4:
            print("method:", method_type[method_type_number]," data:", data[data_type_number], )
            print(method("https://playground.learnqa.ru/ajax/api/compare_query_type",
                         data=str(data[data_type_number])))
            print((method("https://playground.learnqa.ru/ajax/api/compare_query_type",
                         data=str(data[data_type_number]))).url)
            data_type_number += 1
        method_type_number += 1


all_types_and_methods_test()
"""
        if type_number !=0:
            data_number = 0
            print(requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST"))
        else:
            response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                        data="POST")
"""
# def post_type_methods_tests():
# types_and_methods_test()
