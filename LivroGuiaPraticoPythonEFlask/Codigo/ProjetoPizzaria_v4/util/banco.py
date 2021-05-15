# coding: utf-8
import dataset

class Banco:
	def saveUsuario(self, nome, usuario, senha, tipo):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			if ( self.getUsuario(usuario, senha) ):
				return False
			else:
				return db['usuario'].insert(dict(nome=nome, usuario=usuario, senha=senha, tipo=tipo))
		
	def getUsuario(self, usuario, senha):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			usuario = db['usuario'].find_one(usuario=usuario, senha=senha)
			
			if usuario:
				return usuario
			else:
				return False

	def listPizzas (self):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pizzas = db['pizzas'].all()
			return pizzas
			
	def getPizza (self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pizza = db['pizzas'].find_one(id=id)
			
			if pizza:
				return pizza
			else:
				return False
	
	def savePizza(self, nome, descricao):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pizzas'].insert(dict(nome=nome, descricao=descricao, status='ativo'))	
			
	def updatePizza(self, id, nome, descricao, status):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pizzas'].update(dict(id=id, nome=nome, descricao=descricao, status=status), ['id'])	
			
	def deletePizza(self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pizzas'].delete( id=id )
