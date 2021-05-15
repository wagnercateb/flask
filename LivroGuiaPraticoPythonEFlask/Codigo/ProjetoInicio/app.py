# coding: utf-8
from flask import Flask, render_template

app = Flask("projeto01")

@app.route("/")
def ola_mundo():
    return "Olá Mundo! Esse é meu primeiro WebApp!", 200
	
@app.route("/modelo/")
def modelo():
	return render_template("modelo_template.html"), 200
	
@app.route("/variavel/")
def variavel():
	meu_nome = "Wallace Fragoso"
	return render_template("modelo_variavel.html", nome=meu_nome), 200
	
@app.route("/condicional/")
def condicional():
	return render_template("modelo_condicional.html"), 200
	
@app.route("/repeticao/")
def repeticao():
	return render_template("modelo_repeticao.html"), 200

@app.errorhandler(404)
def nao_encontrado(error):
    return render_template('modelo_nao_encontrado.html'), 404

app.run(debug=True, use_reloader=True)