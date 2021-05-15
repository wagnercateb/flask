# coding: utf-8
from flask import Blueprint, render_template, session, request, redirect, url_for
from util.banco import Banco

bp_pedidos = Blueprint('pedidos', __name__, url_prefix='/pedidos')
banco = Banco()

@bp_pedidos.route('/lista/')
def lista():
	if session['usuario']['tipo'] == 'gerente':
		lista = banco.listPedidos()
		return render_template("pedidos/lista.html", lista=lista, banco=banco), 200
	else:
		lista = banco.listPedidosClientes(session['usuario']['id'])
		return render_template("pedidos/lista_clientes.html", lista=lista, banco=banco), 200

@bp_pedidos.route('/cadastro/')
@bp_pedidos.route('/cadastro/<int:id>')
def cadastro( id = None ):
	dados = {'id':'','nome':'','descricao':''}
	pizzas = banco.listPizzas()
	if id :
		dados = banco.getPizza( id )
	
	return render_template("pedidos/cadastro.html", pedido=[], pizzas=pizzas), 200
	
@bp_pedidos.route('/salvar/', methods=['POST'])
def salvar():
	if request.method == "POST":
		if request.form['id'] and request.form['id'] != '' :
			banco.updatePedido(request.form['id'], request.form['pizza'], request.form['preco'], request.form['usuario'])
		else:
			banco.savePedido(request.form['pizza'], request.form['preco'], request.form['usuario'])
	return redirect(url_for('pedidos.lista'))

@bp_pedidos.route('/excluir/')
@bp_pedidos.route('/excluir/<int:id>')
def excluir( id = None ):
	if id:
		banco.deletePedido(id)
	return redirect(url_for('pedidos.lista'))
	
@bp_pedidos.route('/status/')
@bp_pedidos.route('/status/<int:id>')
@bp_pedidos.route('/status/<int:id>/<int:status>')
def status( id = None, status = None):
	if status == 1:
		banco.statusPedido(id, status)
	elif status == 2:
		banco.statusPedido(id, status)
	elif status == 3:
		banco.statusPedido(id, status)
	return redirect(url_for('pedidos.lista'))