# coding: utf-8
from flask import Blueprint

bp_index = Blueprint('index', __name__)

@bp_index.route('/')
def index():
    return u"Olá Projeto Blueprint!", 200