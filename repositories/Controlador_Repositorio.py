import requests

# Clase que gestiona la interacción con el servidor remoto de NodeJs
class Controlador_Repositorio:
	server_url = "https://protoapinode.herokuapp.com"
	user_id = ""

	def __init__(self):
		self.user_id = "0f759dd1ea6c4c76cedc299039ca4f23"

	def save_object(self,data_object):
		object_body = {
			"userId": self.user_id,
			"object": data_object
		}
		sourceDb = f"{self.server_url}/api/graph/{self.user_id}"
		data = requests.post(sourceDb,json = object_body)
		return data.json()

	def get_objects(self):
		sourceDb = f"{self.server_url}/api/graphs/{self.user_id}"
		data = requests.get(sourceDb)
		return data.json()

	def update_object(self,object_id,data_object):
		object_body = {
			"userId": self.user_id,
			"object": data_object
		}
		sourceDb = f"{self.server_url}/api/graph/{object_id}"
		data = requests.put(sourceDb,json = object_body)
		return data.json()

	def delete_object(self,object_id):
		sourceDb = f"{self.server_url}/api/graph/{object_id}"
		data = requests.delete(sourceDb)
		return data.json()