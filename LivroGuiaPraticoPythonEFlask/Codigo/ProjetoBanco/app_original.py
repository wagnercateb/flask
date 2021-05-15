# coding: utf-8
from flask import Flask
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///primeirobanco.db')

@app.route('/')
def index():
    return "Olá SQLite!", 200

app.run(debug=True, use_reloader=True)