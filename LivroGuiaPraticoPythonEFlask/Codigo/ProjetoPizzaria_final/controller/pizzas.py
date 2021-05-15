# coding: utf-8
from flask import Blueprint, render_template, session, request, redirect, url_for
from util.banco import Banco

bp_pizzas = Blueprint('pizzas', __name__, url_prefix='/pizzas')
banco = Banco()

@bp_pizzas.route('/lista/')
def lista():
	lista = banco.listPizzas()
	return render_template("pizzas/lista.html", lista=lista), 200
	
@bp_pizzas.route('/cadastro/')
@bp_pizzas.route('/cadastro/<int:id>')
def cadastro( id = None ):
	dados = {'id':'','nome':'','descricao':''}
	if id :
		dados = banco.getPizza( id )
	
	return render_template("pizzas/cadastro.html", pizza = dados), 200

@bp_pizzas.route('/salvar/', methods=['POST'])
def salvar():
	if request.method == "POST":
		if request.form['id'] and request.form['id'] != '' :
			banco.updatePizza(request.form['id'], request.form['nome'], request.form['descricao'], 'ativo')
		else:
			banco.savePizza(request.form['nome'], request.form['descricao'])
		#return render_template("pizzas/cadastro.html", pizza = dados, msg = u"Cadastro realizado com sucesso!"), 200
	return redirect(url_for('pizzas.lista'))
	
@bp_pizzas.route('/excluir/')
@bp_pizzas.route('/excluir/<int:id>')
def excluir( id = None ):
	if id:
		banco.deletePizza(id)
	return redirect(url_for('pizzas.lista'))
