# coding: utf-8
from flask import Flask
import dataset

app = Flask(__name__)
db = dataset.connect('sqlite:///primeirobanco.db')

@app.route('/')
def index():
	pessoa = db['pessoa']
	return u"Olá SQLite", 200
	
@app.route('/cadastrar_pessoa/')
def pessoa():
	pessoa = db['pessoa']
	pessoa.insert(dict(nome="Wallace", idade=30))
	pessoa.insert(dict(nome="Vanessa", idade=45))
	pessoa.insert(dict(nome="Paula", idade=21))
	pessoa.insert(dict(nome="Arthur", idade=18))
	pessoa.insert(dict(nome="Miguel", idade=31))
	
	return u"Cadastrando uma várias pessoas na tabela <b>PESSOA</b>", 200

@app.route('/listar_tudo/')
def listartudo():
	lista = db['pessoa'].all()
	html = u"Listando tudo!<br>"
	
	for linha in lista:
		html = html + str(linha['id']) + u" - Nome: " + linha['nome'] + u" - Idade: " + str(linha['idade']) + u"<br>"
	return html, 200
	
@app.route('/listar_um/')
def listarum():
	linha = db['pessoa'].find_one(nome="Wallace")
	html = u"Listando um!<br>"
	html = html + str(linha['id']) + u" - Nome: " + linha['nome'] + u" - Idade: " + str(linha['idade']) + u"<br>"
	return html, 200
	
@app.route('/listar_com_filtros/')
def listarcomfiltros():
	#lista = db['pessoa'].find(_limit=2, order_by='nome', _offset=2)
	lista = db.query('SELECT * FROM pessoa')
	html = u"Listando com filtros!<br>"
	
	for linha in lista:
		html = html + str(linha['id']) + u" - Nome: " + linha['nome'] + u" - Idade: " + str(linha['idade']) + u"<br>"
	return html, 200
	
@app.route('/atualizar/')
def atualizar():
	db['pessoa'].update(dict(id=1,idade=40), ['id'])
	return u"Alterando a idade da pessoa <b>Wallace</b> para 40.", 200

@app.route('/excluir/')
def excluir():
	db['pessoa'].delete(id=5)
	return u"Excluindo o registro com id<b>5</b>.", 200
	
app.run(debug=True, use_reloader=True)