# TODO: проверка на пустой ввод
# main.py
import datetime
import requests


def sum(a, b):
    return a + b


# мой первый код
print("моя первая программа =)")

bukva_iks = 5
y = 10
total = sum(bukva_iks, y)  # доступно
print("cумма:", total)

# requests
response = requests.get("https://httpbin.org/get")
print("cтатус код ответа:", response.status_code)
print("длина текста ответа:", len(response.text))


print("=" * 40)
print("сейчас:", datetime.datetime.now().strftime("%d.%m.%Y %H:%M"))
print("=" * 40)
