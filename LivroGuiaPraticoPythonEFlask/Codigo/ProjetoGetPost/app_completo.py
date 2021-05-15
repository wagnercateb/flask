# coding: utf-8
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html"), 200

@app.route("/form_get/")
def form_get():
    return render_template("formulario_get.html"), 200

@app.route("/form_post/")
def form_post():
    return render_template("formulario_post.html"), 200

@app.route("/resultado/", methods=['GET','POST'])
def resultado():
	if request.method == "GET":
		return "Get", 200
	elif request.method == "POST":
		nome = request.form['nome']
		idade = request.form['idade']
		return "Nome: {} - Idade: {}<br>Post".format(nome, idade), 200
	else: 
		return "Não definido", 200

@app.route("/api/")
@app.route("/api/<versao>/")
@app.route("/api/<versao>/<metodo>/")
@app.route("/api/<versao>/<metodo>/<pagina>/")
def api(versao = None, metodo = None, pagina = None):
    return "Versao: {}<br> Metodo: {}<br> Página: {}".format(versao, metodo, pagina), 200

app.run(debug=True, use_reloader=True)