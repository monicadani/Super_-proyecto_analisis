from flask import Flask
from flask_cors import CORS
from routes.Rutas_Grafo import Rutas_Grafo
from repositories.Controlador_Repositorio import Controlador_Repositorio

app = Flask(__name__)
CORS(app)
controlador = Controlador_Repositorio()
rutas = Rutas_Grafo(controlador).get_routes()
app.register_blueprint(rutas)

if __name__ == '__main__':
	app.run(debug=True, host="localhost", port=7000)



