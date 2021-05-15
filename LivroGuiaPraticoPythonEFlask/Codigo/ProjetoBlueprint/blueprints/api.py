# coding: utf-8
from flask import Blueprint

bp_api = Blueprint('api', __name__)

@bp_api.route('/api/')
def api():
    return u"Olá Você está na página da API!", 200