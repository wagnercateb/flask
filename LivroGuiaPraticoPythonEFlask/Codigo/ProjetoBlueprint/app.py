# coding: utf-8
from flask import Flask
from blueprints.index import bp_index
from blueprints.api import bp_api
from blueprints.converter import bp_converter

app = Flask(__name__)
app.register_blueprint(bp_index)
app.register_blueprint(bp_api)
app.register_blueprint(bp_converter)

app.run(debug=True, use_reloader=True)