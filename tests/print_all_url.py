import requests

def print_all_url():
    response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
    amount = response.history
    #first_resp = response.history[0]
    #sec_resp = response.history[1]
    # print(first_resp.url)
    # print(sec_resp.url)
    u = 0
    while u < (len(response.history)):
        print(response.history[u].url)
        u +=1


print_all_url()