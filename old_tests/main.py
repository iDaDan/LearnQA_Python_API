
import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
amount = len(response.history)
last_url = response.history[amount - 2].url


# print("Редиректов:"+str(amount)+", последний урл: "+last_url)


# Скрипт для ex7: запросы и методы
def types_and_methods_test():
    response_get_no_papam = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print("post, no data:")
    print(response_get_no_papam.text)
    print(response_get_no_papam)

    response_get_no_param_head_test = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print("head, no data:")
    print(response_get_no_param_head_test.text)
    print(response_get_no_param_head_test)


    response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                data={"method":"POST"})
    print("post, data post")
    print(response_get_type_post_test.text)
    print(response_get_type_post_test)

    response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                data={"method":"DELETE"})
    print("post, data Delete:")
    print(response_get_type_post_test.text)
    print(response_get_type_post_test)

types_and_methods_test()