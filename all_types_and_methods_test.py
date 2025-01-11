import requests


def all_types_and_methods_test():
    true_method_type = ["get", "post", "put", "delete"]
    true_method_type_number = 1

    while true_method_type_number < 4:
        true_method = getattr(requests, true_method_type[true_method_type_number])
        mischieving_method_type = ["GET", "POST", "PUT", "DELETE"]
        mischieving_method_type_number = 1
        response = true_method("https://playground.learnqa.ru/ajax/api/compare_query_type",
                               data={"method": mischieving_method_type[mischieving_method_type_number]})
        while mischieving_method_type_number < 4:
            print(
                f"true method type: {true_method_type[true_method_type_number]}, true_method response: {response}, "
                f"true_method response.text: {response.text}, "
                f"mischieving_method_type: {mischieving_method_type[mischieving_method_type_number]}")

            mischieving_method_type_number += 1
        true_method_type_number += 1

        # if type_number !=0:
        #     data_number = 0
        #     print(requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", mischieving_method_type="POST"))
        # else:
        #     response_get_type_post_test = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type",
        #                                                 mischieving_method_type="POST")


all_types_and_methods_test()
