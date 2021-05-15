# coding: utf-8
from flask import Blueprint, render_template

bp_site = Blueprint('site', __name__)

@bp_site.route('/')
def site():
    return render_template("site/index.html"), 200