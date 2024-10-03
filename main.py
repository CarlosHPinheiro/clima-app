import requests

def get_data(url, cidade, API_KEY):
    request = requests.get(url)
    response = request.json()
    
    clima = response['weather'][0]['description'].title()
    temperatura = int(response['main']['temp'])
    umidade = response['main']['humidity']
    cidade = response['name']
    vento = response["wind"]["speed"]
    pais = response["sys"]["country"]
    pais = f"https://flagsapi.com/{pais}/flat/64.png"
    icon = response['weather'][0]["icon"]
    icon = f"https://openweathermap.org/img/wn/{icon}.png"

    return {"clima": clima, "temperatura": temperatura, "umidade": umidade, "cidade": cidade, "vento": vento, "pais": pais, "icon": icon}
