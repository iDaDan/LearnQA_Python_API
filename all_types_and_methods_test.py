import requests

def all_types_and_methods_test():
    method_type = ["get", "post", "put", "delete"]
    data = ["GET", "POST", "PUT", "DELETE"]
    data_type_number = 1
    # рабочая конкретная строка:
    method_type = ["get", "post", "put", "delete"]
    method_type_number = 1
    method = getattr(requests, method_type[method_type_number])
    data = ["GET", "POST", "PUT", "DELETE"]
    data_type_number = 1
    responser = method("https://playground.learnqa.ru/ajax/api/compare_query_type",
                    params={"method": method_type[method_type_number]})

    print("method:", method_type[method_type_number], responser," response.text:", responser.text, " data_not_data:", data[data_type_number])
    #method_name in method_type:

    # print("method:", method_type[method_type_number], " data:", data[data_type_number], )
    # print(method("https://playground.learnqa.ru/ajax/api/compare_query_type",
    #              data=str(data[data_type_number])))
    # print((method("https://playground.learnqa.ru/ajax/api/compare_query_type",
    #               data=str(data[data_type_number]))).url)


    # method_type = ["get", "post", "put", "delete"]
    # method_type_number = 1
    # while method_type_number < 4:
    #     method = getattr(requests, method_type[method_type_number])
    #     data = ["GET", "POST", "PUT", "DELETE"]
    #     data_type_number = 1
    #     while data_type_number < 4:
    #         print("method:", method_type[method_type_number]," data:", data[data_type_number], )
    #         print(method("https://playground.learnqa.ru/ajax/api/compare_query_type",
    #                      data=str(data[data_type_number])))
    #         print((method("https://playground.learnqa.ru/ajax/api/compare_query_type",
    #                      data=str(data[data_type_number]))).url)
    #         data_type_number += 1
    #     method_type_number += 1


        # if type_number !=0:
        #     data_number = 0
        #     print(requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST"))
        # else:
        #     response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
        #                                                 data="POST")


all_types_and_methods_test()