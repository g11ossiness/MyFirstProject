# main.py
def sum(a, b):
    return a + b

# певрый код
print("моя первая программа =)")

x = 5
y = 10
total = sum(x, y)  # доступно
print("Сумма:", total)

# requests 
import requests
response = requests.get("https://httpbin.org/get")
print("Статус код ответа:", response.status_code)
print("Длина текста ответа:", len(response.text))