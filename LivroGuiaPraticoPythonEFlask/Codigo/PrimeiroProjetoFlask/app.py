# coding: utf-8
from flask import Flask, request, render_template, escape, session
import dataset

db = dataset.connect('sqlite:///teste.db')
dbteste = db['teste']

#app = Flask("PrimeiroProjetoFlask")
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # nessário para a criação da sessão

@app.route('/')
def index():
    return render_template("index.html"), 200

@app.route("/usuario/")
@app.route("/usuario/<name>/")
def usuario(name=None):
    return render_template("usuario.html", name=name, categoria=request.args.get("categoria")), 200

@app.route('/formulario/')
def formulario():
    return render_template("formulario.html"), 200

@app.route('/formulario_post/', methods=['POST'])
def formulario_post():
    return render_template("formulario_post.html"), 200

@app.route('/sessao/')
def sessao():
    session['usuario'] = {"usuario":"wallace", "senha":"123"}
    return render_template("sessao.html"), 200


@app.route('/banco/')
def banco():
    '''
    return u"""
            <h1>Noticia id %s inserida com sucesso!</h1>
            <a href="%s"> Inserir nova notícia </a>
        """ % (dbteste.insert({"nome":"wallace","idade":"30"}), '/banco/')
    '''
    return render_template("banco.html"), 200

@app.route('/banco_listar/')
def banco_listar():
    base_html = u"""
      <html>
      <head>
          <title>{title}</title>
      </head>
      <body>
         {body}
      </body>
      </html>
    """

    noticia_template = u"""
        <a href="/pessoa/{lista[id]}">{lista[nome]} - {lista[idade]}</a>
    """

    # it's a kind of magic :)
    todas_as_noticias = [
        noticia_template.format(lista=lista)
        for lista in dbteste.all()
    ]

    return base_html.format(
        title=u"Todas as informações",
        body=u"<br />".join(todas_as_noticias)
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template('nao_encontrado.html'), 404

app.run(debug=True, use_reloader=True)
