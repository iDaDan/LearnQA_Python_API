import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
amount = len(response.history)
last_url = response.history[amount-2].url

#print("Редиректов:"+str(amount)+", последний урл: "+last_url)


#Скрипт для ex7: запросы и методы
def types_and_methods_test():
    response_get_no_papam = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response_get_no_papam)
    print(response_get_no_papam.url)

    response_get_no_param_head_test = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response_get_no_param_head_test)
    print(response_get_no_param_head_test.url)

    response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST")
    print(response_get_type_post_test)
    print(response_get_type_post_test.url)

def all_types_and_methods_test():
    method_type = ["get", "post", "put", "delete"]
    data = ["GET", "POST", "PUT", "DELETE"]
    type_number = 0
    data_number = 0
    hell_and_heaven_epic_divider = 0

    while type_number<4:
        type = method_type[type_number]
        if type_number !=0:
            data_number = 0
            print(requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST"))
        else:
            response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
                                                        data="POST")



types_and_methods_test()