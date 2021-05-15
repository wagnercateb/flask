# coding: utf-8
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'MINHA_CHAVE_SECRETA' # nessário para a criação da sessão

@app.route('/')
def index():
    return "Olá Sessão", 200

app.run(debug=True, use_reloader=True)