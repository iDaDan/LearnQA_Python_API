import time
import requests
import json

def tokens_test():
    # создаём кипучую задачу
    resp=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    print(resp.text)
    # {"token":"AMxoDMzojMxAyMx0SMw0SNyAjM","seconds":15}
    obj = json.loads(resp.text)
    token = obj["token"]
    seconds_till_end = obj["seconds"]
    print(token)
    correct_status_not_ready = "Job is NOT ready"
    correct_status_ready = "Job is ready"

    # теребим задачу пока не готова, для этого подставляем кипучий токен, проверяем что status Job is NOT ready
    resp_not_ready=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
    resp_not_ready_text = json.loads(resp_not_ready.text)
    print(resp_not_ready_text)
    resp_not_ready_fact_status = resp_not_ready_text["status"]
    print(f"{resp_not_ready_fact_status} ?== {correct_status_not_ready}")
    if resp_not_ready_fact_status == correct_status_not_ready:
        print("Статус отображается корректно")
    else:
        print("Статус отображается НЕ корректно")

    # усыпляем на количество секунд из первого метода, проверяем что status Job is NOT ready
    time.sleep(seconds_till_end+1)
    resp_ready=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
    resp_ready_text = json.loads(resp_ready.text)
    print(resp_ready_text)
    resp_ready_fact_status = resp_ready_text["status"]
    if resp_ready_fact_status == correct_status_ready:
        print("Статус готовности отображается корректно")
    else:
        print("Статус готовности отображается НЕ корректно")

tokens_test()