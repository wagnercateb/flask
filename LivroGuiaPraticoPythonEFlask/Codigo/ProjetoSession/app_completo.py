# coding: utf-8
from flask import Flask, request, redirect, session, url_for, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'MINHA_CHAVE_SECRETA' # nessário para a criação da sessão

@app.route('/')
def index():
	html = '''<h1>Bem vindo ao Projeto Sessão</h1><p>Essa é a tela principal, logo abaixo veremos se você está <i>Logado</i></p>'''
	
	if 'usuario' in session:
		return html + '<p>Parabéns! Você está logado com o usuário {}. <a href="{}">Sair</a></p>'.format(session['usuario'],url_for('logout'))
	return html + '<p>Você não está logado, por favor acesse a área de <a href="'+ url_for('login') +'">Login</a>.</p>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['usuario'] = request.form['usuario']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Usuário: <input type=text name=usuario> <br>
            <input type=submit value=Entrar>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

@app.route('/restrito')
def restrito():
	if 'usuario' in session:
		return 'Olá {}, <br> Você está autorizado a acessar está área.'.format(session['usuario'])
	return redirect(url_for('index'))

app.run(debug=True, use_reloader=True)