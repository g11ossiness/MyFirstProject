# main.py
def sum(a, b):
    return a + b

# певрый код
print("моя первая программа =)")

x = 5
y = 10
total = sum(x, y)  # доступно
print("cумма:", total)

# requests 
import requests
response = requests.get("https://httpbin.org/get")
print("cтатус код ответа:", response.status_code)
print("длина текста ответа:", len(response.text))

import datetime

print("=" * 40)
print("сейчас:", datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
print("=" * 40)