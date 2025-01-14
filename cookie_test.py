import json

import requests
from bs4 import BeautifulSoup

payload = {"login":"super_admin", "password":""}
response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
cookie_value = response.cookies.get("auth_cookie")
print(cookie_value)
#cookies = {}
passwords_list_raw_info = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
passwords_list_cookie_raw_info = passwords_list_raw_info.cookies.get("Top 25 most common passwords by year according to SplashData")
obj = json.loads(passwords_list_cookie_raw_info)

#passwords_list = passwords_list_cookie_raw_info.cookies.get("Top 25 most common passwords by year according to SplashData")
#soup = BeautifulSoup(passwords_list_raw_info.text)
# jija = soup('class="wikitable",'jijalxml").find_all('class="wikitable","lxml")
# print(jija)
#print(passwords_list_raw_info.text)



# if cookie_value is not None:
#     cookies.update() #тут точно нужен корректный логин, но может и не корректный, тогда метод придётся рихтовать

# checked_response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = cookie_value)
# print(checked_response,checked_response.text)

# payload = {"login":"secret_login", "password":"secret_pass2"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data = payload)
#
# cookie_value = response1.cookies.get("auth_cookie")
# cookies = {}
#
# if cookie_value is not None:
#     cookies.update({"auth_cookie":cookie_value})
#
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies = cookies)
#
#
# print(response2.text, "111")