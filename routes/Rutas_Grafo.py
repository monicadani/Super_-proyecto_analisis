from flask import Blueprint, request, render_template
from models.Grafo import Grafo
import random

class Rutas_Grafo:
	def __init__(self,repository):
		self.repo = repository

	def get_routes(self):
		rutas_grafo = Blueprint('rutas_grafo', __name__)

		@rutas_grafo.route('/restApi/grafo/random/<int:size>', methods=['GET'])
		def grafo_aleatorio(size):
			# Se crea el grafo
			new_grafo = Grafo({
				"nombre": "Grafo random",
				"tipo": "Aleatorio",
			})

			# Se crean los nodos de forma aleatoria
			num_nodos = size +1
			for i in range(1, num_nodos):
				new_grafo.get_nodos().append({
					"id": i,
					"dato": random.choice(["AND", "OR", "NOT", "XOR", "NAND", "NOR", "XNOR"])
				})

			# Se crean las aristas de forma aleatoria
			num_aristas = random.randint(num_nodos, num_nodos * 2)

			num_nodo = 1
			for i in range(num_aristas):
				if(i > num_nodos):
					num_nodo = 1
				new_grafo.get_aristas().append({'inicio': num_nodo, 'fin': random.choice(new_grafo.get_nodos())["id"], 'peso': i})
				num_nodo += 1


			return new_grafo.get_json()



			"""num_aristas = random.randint(num_nodos,num_nodos*2)
			for i in range(num_aristas):
				new_grafo.get_aristas().append({"id":i,"peso":i})
			num_nodo = 1
			for i in range(num_aristas):
				if(i > num_nodos):
					num_nodo = 1
				new_grafo.get_adyacencias().append({
					"inicio":num_nodo,
					"destino":random.choice(new_grafo.get_nodos())["id"],
					"arista":i
				})
				num_nodo += 1 """

		@rutas_grafo.route('/')
		def index():
			return render_template('index.html')

		@rutas_grafo.route('/restApi/grafos', methods=['GET'])
		def enlistar_grafos():
			return self.repo.get_objects()

		@rutas_grafo.route('/restApi/grafo', methods=['POST'])
		def almacenar_grafo():
			grafo = Grafo(request.json)
			grafo.set_json(request.json)
			return self.repo.save_object(grafo.get_json())

		@rutas_grafo.route('/restApi/grafo/<string:id>', methods=['PUT'])
		def actualizar_grafo(id):
			grafo = Grafo(request.json)
			grafo.set_json(request.json)
			return self.repo.update_object(id,grafo.get_json())
			
		@rutas_grafo.route('/restApi/grafo/<string:id>', methods=['DELETE'])
		def eliminar_grafo(id):
			return self.repo.delete_object(id)

		return rutas_grafo