import requests

API_KEY = ""

def get_data(url, cidade, API_KEY):
    request = requests.get(url)
    response = request.json()
    print(response)

    clima = response['weather'][0]['description'].title()
    temperatura = response['main']['temp']
    temperatura = f'{temperatura:.1f}'
    umidade = response['main']['humidity']
    cidade = response['name']
    vento = response["wind"]["speed"]
    pais = response["sys"]["country"]

    return {"clima": clima, "temperatura": temperatura, "umidade": umidade, "cidade": cidade, "vento": vento, "pais": pais}
