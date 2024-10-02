from flask import Flask, render_template, request
from main import get_data, API_KEY


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/clima", methods=['GET'])
def clima():
    cidade = request.args.get('cidade')

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    data = get_data(url, cidade, API_KEY)

    return render_template(f"clima.html", cidade = data["cidade"], temperatura = data["temperatura"], clima = data["clima"], umidade = data["umidade"], vento = data["vento"])


if __name__ == ("__main__"):
    app.run(debug=True)
