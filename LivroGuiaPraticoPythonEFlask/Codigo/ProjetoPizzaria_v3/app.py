# coding: utf-8
from flask import Flask, session
from controller.site import bp_site
from controller.usuario import bp_usuario
from controller.gerencia import bp_gerencia

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(bp_site)
app.register_blueprint(bp_usuario)
app.register_blueprint(bp_gerencia)

app.run(debug=True, use_reloader=True)