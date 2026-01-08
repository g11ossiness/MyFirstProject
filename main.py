# main.py
def sum(a, b):
    return a + b

# певрый код =)
print("МОЯ ПЕРВАЯ ПРОГРАММА =)")

x = 5
y = 10
total = sum(x, y)  # доступно
print("СУММА:", total)

# requests 
import requests
response = requests.get("https://httpbin.org/get")
print("СТАТУС ОТВЕТА:", response.status_code)
print("ДЛИНА ОТВЕТА:", len(response.text))

import datetime

print("=" * 40)
print("СЕЙЧАС:", datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
print("=" * 40)