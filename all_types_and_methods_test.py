import requests

def all_types_and_methods_test():
    true_method_var = ["get", "post", "put", "delete"]
    # true_method_type_number = 1
    for true_method in true_method_var:
        mischieving_method_var = ["GET", "POST", "PUT", "DELETE"]
        for mischieving_method in mischieving_method_var:
            if true_method != "get":
                data = {"method": mischieving_method}
                params = None
            else:
                data = None
                params = {"method": mischieving_method}
                # mischieving_method = "params"
            method = getattr(requests, true_method)
            # mischieving_method_type_number = 0
            response = method("https://playground.learnqa.ru/ajax/api/compare_query_type",
                              params=params,
                              data=data)
            print(
                f"true method type: {true_method}, true_method response: {response}, "
                f"true_method response.text: {response.text}, "
                f"mischieving_method_var: {mischieving_method}")

            # mischieving_method_type_number += 1
        # true_method_type_number += 1

all_types_and_methods_test()
