import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
amount = len(response.history)
last_url = response.history[amount-1].url

print("Редиректов:"+str(amount)+", последний урл: "+last_url)
