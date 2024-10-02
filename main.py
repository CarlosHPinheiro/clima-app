import requests

API_KEY = "39476510ebd34b2d6e6db19947564172"
city = "Santos"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br"

request = requests.get(url)
response = request.json()

if request.status_code == 404:
    print("Cidade não encontrada")

weather = response['weather'][0]['main']
description = response['weather'][0]['description']
temperature = response['main']['temp']
humidity = response['main']['humidity']
city_name = response['name']

print(f'Cidade: {city_name} \nTemperatura: {temperature:.1f}°C \nClima: {weather} - {description} \nUmidade relativa do ar: {humidity}%')
