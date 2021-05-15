# coding: utf-8
from flask import Blueprint, render_template, session, request, redirect, url_for
from util.banco import Banco

bp_gerencia = Blueprint('gerencia', __name__, url_prefix='/gerencia')
banco = Banco()

@bp_gerencia.route('/registro/')
def gerencia_registro():
    return render_template("gerencia/registro.html"), 200