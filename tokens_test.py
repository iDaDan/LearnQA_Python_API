import requests

def tokens_test():
    # создаём кипучую задачу
    resp=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    print(resp.text)
    # теребим задачу пока не готова, для этого подставляем кипучий токен, проверяем что status Job is NOT ready
    resp_not_ready_status=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    # усыпляем на количество секунд из первого метода, проверяем что status Job is NOT ready
    resp_result_status = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")


tokens_test()