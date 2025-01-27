import requests
from lxml import html

payload = {"login":"super_admin", "password":""}
response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
cookie_value = response.cookies.get("auth_cookie")
passwords_list_raw_info = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")

# Полупонятная магия из https://gist.github.com/KotovVitaliy/86ce86538f36b291a48347a2552573ad#gist-pjax-container,
# нужно разобраться позже:
tree = html.fromstring(passwords_list_raw_info.text) #вот это основное, локатор плюс-минус

# локатор, видимо, подходит для всех td[@align="left"]
# дочерних для [contains(text(),"Top 25 most common passwords by year according to SplashData")]
# но почему/как passwords сразу складывает их в массив?
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()' #Ds
passwords = tree.xpath(locator)

for password in passwords:
    print(f"password2{password}")
    password = str(password).strip()
    print(password)

# passwords_list_cookie_raw_info = passwords_list_raw_info.cookies.get("Top 25 most common passwords by year according to SplashData")
# obj = json.loads(str(passwords_list_cookie_raw_info))
# print(obj)



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