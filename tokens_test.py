import requests

def tokens_test():
    resp=requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
    print(resp.text)

tokens_test()