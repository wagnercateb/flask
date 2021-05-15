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

#para gerar link para esta route, passe o nome da função para a function url_for: url_for('resultado2')    (e náo `resultado1`)
@app.route("/resultado1/", methods=['GET','POST'])
def resultado2():
	if request.method == "GET":
		# Hardcoding URLs in the templates and view functions is a bad practice
		return 'Get <br/> <a href="/">Página inicial</a>', 200
	elif request.method == "POST":
		return "Post", 200
	else: 
		return "Não definido", 200

#essa route mostra como o conteúdo é recebido
@app.route('/recebendo_dados_post/', methods=['POST'])
def recebe_e_mostra_os_dados():
    return render_template("recebe_post.html"), 200

app.run(debug=True, use_reloader=True)