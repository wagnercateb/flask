# coding: utf-8
from flask import Blueprint, render_template
from util.banco import Banco

bp_site = Blueprint('site', __name__)
banco = Banco()

@bp_site.route('/')
def site():
	lista = banco.listPizzas()
	return render_template("site/index.html", lista=lista), 200