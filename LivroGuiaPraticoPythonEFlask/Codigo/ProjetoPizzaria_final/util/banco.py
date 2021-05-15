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
				
	def getUsuarioID(self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			usuario = db['usuario'].find_one(id=id)
			
			if usuario:
				return usuario
			else:
				return False

	def listPizzas (self):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pizzas = db['pizzas'].all()
			if db['pizzas'].count() > 0 :
				return pizzas
			else:
				return False
			
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
			
	def listPedidos (self):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pedidos = db['pedidos'].all()
			
			if db['pedidos'].count() > 0 :
				return pedidos
			else:
				return False
	
	def listPedidosClientes (self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pedidos = db['pedidos'].find(usuario=id)
			
			if db['pedidos'].count(usuario=id) > 0 :
				return pedidos
			else:
				return False
	
	def getPedido (self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			pedidos = db['pedidos'].find_one(id=id)
			
			if pedidos:
				return pedidos
			else:
				return False
	
	def savePedido(self, pizza, preco, usuario):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pedidos'].insert(dict(usuario=usuario, codigo_pizza=pizza, tamanho_valor=preco, status='Pendente'))	
			
	def updatePedido(self, id, pizza, preco, usuario):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pedidos'].update(dict(id=id, usuario=usuario, codigo_pizza=pizza, tamanho_valor=preco), ['id'])	
			
	def deletePedido(self, id):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			return db['pedidos'].delete( id=id )
	
	def statusPedido(self, id, status):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			if status == 1:
				return db['pedidos'].update(dict(id=id, status='Pronto para envio'), ['id'])
			elif status == 2:
				return db['pedidos'].update(dict(id=id, status='Entregue'), ['id'])
			elif status == 3:
				return db['pedidos'].update(dict(id=id, status='Concluido'), ['id'])
			
	def getValorPedidoDescricao(self, valor):
		if valor == '11.90':
			return u'Broto - R$ 11,90 - 4 Fatias'
		elif valor == '21.90':
			return u'Pequena - R$ 21,90 - 6 Fatias'
		elif valor == '31.90':
			return u'Média - R$ 31,90 - 8 Fatias'
		elif valor == '41.90':
			return u'Grande - R$ 41,90 - 10 Fatias'
		elif valor == '51.90':
			return u'Extra Grande - R$ 51,90 - 12 Fatias'