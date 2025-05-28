from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    code = request.args.get('code')
    if code:
        return f'Código recebido: {code}'
    return 'Aplicativo Flask do Mercado Livre conectado!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
