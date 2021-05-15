# coding: utf-8
from flask import Flask
from controller.site import bp_site

app = Flask(__name__)
app.register_blueprint(bp_site)

app.run(debug=True, use_reloader=True)