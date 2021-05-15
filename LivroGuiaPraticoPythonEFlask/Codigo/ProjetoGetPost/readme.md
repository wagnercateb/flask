# Dicas básicas

### cria ambiente virtual:
python3 -m venv ./venv (o ponto é para diretório oculto) (ou criar no diretório corrente)

### ativa ambiente virtual:
no Linux (ou no terminal bash do VSCode): # source .venv/Scripts/activate (o arquivo não pode se executado diretamente)
no Windows: .venv/Scripts/activate

### dependëncias
Para guardar todas as dependências do projeto: pip freeze > requirements.txt
Para instalar as mesmas dependências no servidor de produção: pip install -r requirements.txt

### para rodar o projeto: python app.py