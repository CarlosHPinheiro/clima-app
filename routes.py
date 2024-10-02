from flask import Flask, render_template, request, redirect, url_for
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

    return render_template(f"clima.html", cidade = data["cidade"], temperatura = data["temperatura"], clima = data["clima"], umidade = data["umidade"], vento = data["vento"], icon = data["icon"], pais = data["pais"])


# Tratamento de erros
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))


@app.errorhandler(500)
def internal_server_error(e):
    return redirect(url_for('index'))


@app.errorhandler(KeyError)
def handle_key_error(e):
    return redirect(url_for('index'))


if __name__ == ("__main__"):
    app.run(debug=True)
