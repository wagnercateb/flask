# coding: utf-8
import dataset

class Banco:
	def saveUsuario(self, nome, usuario, senha):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			if ( self.getUsuario(usuario, senha) ):
				return False
			else:
				return db['usuario'].insert(dict(nome=nome, usuario=usuario, senha=senha))
		
	def getUsuario(self, usuario, senha):
		with dataset.connect('sqlite:///pizzaria.db') as db:
			usuario = db['usuario'].find_one(usuario=usuario, senha=senha)
			
			if usuario:
				return usuario
			else:
				return False