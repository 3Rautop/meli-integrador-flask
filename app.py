from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "App do Mercado Livre está online!"

@app.route("/meli/callback")
def meli_callback():
    code = request.args.get("code")
    if code:
        return f"Recebi o código: {code}"
    else:
        return "Nenhum código foi recebido."
