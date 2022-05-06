class Grafo():
	nombre = ""
	tipo = ""
	nodos = []
	aristas = []
	adyacencias = []

	def __init__(self, grafo_body):
		self.nombre = grafo_body['nombre']
		self.tipo = grafo_body['tipo']
		self.nodos = []
		self.aristas = []
		self.adyacencias = []

	def set_nodo(self, nodo):
		self.nodos.append(nodo)

	def set_arista(self, arista):
		self.aristas.append(arista)

	def set_adyacencia(self, adyacencia):
		self.adyacencias.append(adyacencia)

	def get_nodos(self):
		return self.nodos

	def get_aristas(self):
		return self.aristas

	def get_adyacencias(self):
		return self.adyacencias

	def get_json(self):
		return {
			'nombre': self.nombre,
			'tipo': self.tipo,
			'nodos': self.nodos,
			'aristas': self.aristas,
			'adyacencias': self.adyacencias
		}

	def set_json(self, json):
		self.nombre = json['nombre']
		self.tipo = json['tipo']
		self.nodos = json['nodos']
		self.aristas = json['aristas']
		self.adyacencias = json['adyacencias']