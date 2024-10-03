from flask import Flask, render_template, request, redirect, url_for
from main import get_data
from dotenv import load_dotenv
import os


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    cidade = request.args.get('cidade')
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

    data = get_data(url, cidade, API_KEY)

    return render_template(f"index.html", cidade = data["cidade"], temperatura = data["temperatura"], clima = data["clima"], umidade = data["umidade"], vento = data["vento"], icon = data["icon"], pais = data["pais"])


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
