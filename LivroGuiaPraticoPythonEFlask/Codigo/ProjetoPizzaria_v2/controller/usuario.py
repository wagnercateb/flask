# coding: utf-8
from flask import Blueprint, render_template, session, request, redirect, url_for
from util.banco import Banco

bp_usuario = Blueprint('usuario', __name__)
banco = Banco()

@bp_usuario.route('/usuario/login/')
def login():
    return render_template("usuario/login.html"), 200

@bp_usuario.route('/usuario/autenticar/', methods=['GET','POST'])
def autenticar():
	if request.method == "GET":
		return render_template("usuario/login.html", erro=u"Não foi possível realizar o login!"), 200
	elif request.method == "POST":
		usuario = banco.getUsuario(request.form['usuario'], request.form['senha'])
		if ( usuario ):
			session['usuario'] = {"nome": usuario['nome'], "usuario": usuario['usuario']}
			return redirect(url_for('site.site'))
		else:
			return render_template("usuario/login.html", erro=u"Usuário ou Senha inválidos!"), 200

@bp_usuario.route('/usuario/registro/')
def registro():
    return render_template("usuario/registro.html"), 200

@bp_usuario.route('/usuario/cadastro/', methods=['GET','POST'])
def cadastro():
	if request.method == "GET":
		return render_template("usuario/erro_cadastro.html"), 200
	elif request.method == "POST":
		if ( banco.saveUsuario(request.form['nome'], request.form['usuario'], request.form['senha']) ):
			session['usuario'] = {"nome": request.form['nome'], "usuario": request.form['usuario']}
			return render_template("usuario/sucesso_cadastro.html"), 200
		else:
			return render_template("usuario/erro_cadastro.html"), 200
		
@bp_usuario.route('/usuario/sair/')
def sair():
    session.pop('usuario', None)
    return redirect(url_for('site.site'))