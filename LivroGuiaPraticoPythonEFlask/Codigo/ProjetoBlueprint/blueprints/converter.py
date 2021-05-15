# coding: utf-8
from flask import Blueprint

bp_converter = Blueprint('converter', __name__)

@bp_converter.route('/converter/')
def converter():
    return u"Olá Você está na página de CONVERTER!", 200