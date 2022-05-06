/*Agregar cambios de colores en creacion y edicion de nodos
Saber diferenciar nodos de aristas
*/




// Creación del diagrama asociado a un DIV
var $ = go.GraphObject.make;
var myDiagram = $(go.Diagram,
	"myDiagramDiv",
	{
		initialAutoScale: go.Diagram.Uniform,
		layout: $(go.CircularLayout,
			{ radius: 100 },
		)
	});

// Parametrización de los nodos
myDiagram.nodeTemplate =
	$(go.Node, "Auto",
		$(go.Shape,
			"Square",
			{ stroke: "gray" },
			new go.Binding("fill", "color")
		),
		new go.Binding("location", "loc"),
		$(go.TextBlock,
			{ margin: 3, font: '20px sans',stroke: 'white' },
			new go.Binding("text", "t")
		)
	);

// Parametrización de las aristas
myDiagram.linkTemplate =
	$(go.Link,
		{ curve: go.Link.Bezier, curviness: 20 },
		new go.Binding("curviness"),
		$(go.Shape),
		$(go.Shape, { toArrow: "Standard" }),
		$(go.Panel, "Auto",
			$(go.Shape, "Ellipse",
				{ fill: "white", stroke: "gray" }
			),
			$(go.TextBlock,
				{ margin: 1, font: '10px sans' },
				new go.Binding("text", "text")
			)
		)
	);

// Modelo inicial del grafo como ejemplo
myDiagram.model = new go.GraphLinksModel(
	[
		{ t: "NOT", key: "1", color: "purple" },
		{ t: "AND", key: "2", color: "orange" },
		{ t: "OR", key: "3", color: "lightgreen" },
		{ t: "XOR", key: "4", color: "pink" }
	],
	[
		{ from: "1", to: "2", text: "2",key:'1_2_2'},
		{ from: "2", to: "1", text: "3" ,key:'2_1_3'},
		{ from: "1", to: "3", text: "5" ,key:'1_3_5'},
		{ from: "2", to: "2", text: "10", key:'2_2_10'},
		{ from: "3", to: "4", text: "20" ,key:'3_4_20'},
		{ from: "4", to: "1", text: "50", key:'4_1_50'}
	]);

let modificarGrafo = (palabra) => {
	console.log('-funciona-')

	myDiagram.model.addNodeData({ t: palabra, key: "4", color: "purple" });
	myDiagram.model.layout.Diagram(true);

}

// Agregación de modelo según un JSON
let setModel = (grafo) => {
	let nodos = [];
	for (let n of grafo.nodos) {
		nodos.push({ t: n.dato, key: n.id, color: "purple" });
	}
	let adyacencias = [];
	for (let n of grafo.adyacencias) {
		adyacencias.push({ from: n.inicio, to: n.destino, text: n.arista });
	}
	myDiagram.model = new go.GraphLinksModel(nodos, adyacencias);
}

// Peticiones al servidor con el uso de Axios
let getRequest = (url) => {
	axios.get(url).then(response => {
		let grafo = response.data;
		console.log(grafo);
		setModel(grafo);
	}).catch(error => {
		console.log(error);
	});
}

let getRequest2 = (url) => {
	axios.get(url).then(response => {
		console.log('--grafos--')
		let grafo = response.data;
		console.log(grafo['data']);
		setModel(grafo.data[0].object[0]);
	}).catch(error => {
		console.log(error);
	});
}

let getRequest3 = (url) => {
	axios.get(url).then(response => {

		let grafo = response.data;
		console.log(grafo['data']);
		setModel(grafo.data[0].object[0]);
	}).catch(error => {
		console.log(error);
	});
}


// Eventos a los botones
document.querySelector("#boton").addEventListener("click", () => {
	getRequest(`http://localhost:7000/restApi/grafo/random/${document.querySelector("#size").value}`);
});

document.querySelector("#boton2").addEventListener("click", () => {
	getRequest2('http://localhost:7000/restApi/grafos');
});

document.querySelector("#boton3").addEventListener("click", () => {
	console.log('-DATOS-')
	console.log(myDiagram.selection.toArray())


});

document.querySelector("#boton4").addEventListener("click", () => {
	alert('boton 4')
});

document.querySelector("#boton5").addEventListener("click", () => {
	alert('boton 5')

});

/*----------Nivel 1 Archivo-------*/


/*Nivel 1-1-1 
Funcion que se encarga de crear un nuevo grafo
*/
document.querySelector("#boton_crear_pers").addEventListener("click", () => {
	nuevo_grafo();
});

function nuevo_grafo() {

	console.log("prueba")
	let nombre_grafo = document.querySelector('#nombre_grafo_pers').value;
	let error = false;
	let des_error = '';

	/*Se comprueba si el nombre es valido y el num de nodos es un numero */
	if (Object.keys(nombre_grafo).length === 0 || Object.keys(nombre_grafo).length >= 30) {
		error = true;
		des_error = des_error + 'Error en el tamaño del nombre'
	}



	if (error == false) {

		reinizializa_grafo();
	}

	else {
		alert(des_error);
	}
}


function reinizializa_grafo() {
	myDiagram.model = new go.GraphLinksModel(
		[
		],
		[
		]);

}



/*Nivel 1-1-2
Funcion que se encarga de crear un grafo aleatorio
*/
document.querySelector("#boton_crear_alea").addEventListener("click", () => {
	nuevo_grafo_aleatorio();
});

function nuevo_grafo_aleatorio() {
	let nombre_grafo = document.querySelector('#nombre_grafo_alea').value;
	let numero_nodos = document.querySelector('#numero_nodos_alea').value;
	let error = false;
	let des_error = '';

	/*Se comprueba si el nombre es valido y el num de nodos es un numero */
	if (Object.keys(nombre_grafo).length === 0 || Object.keys(nombre_grafo).length >= 30) {
		error = true;
		des_error = des_error + 'Error en el tamaño del nombre'
	}

	if (isNaN(numero_nodos) || Object.keys(nombre_grafo).length === 0) {
		error = true;
		des_error = des_error + ', el numero de nodos no es un numero valido'
	}


	if (error == false) {
		getRequest(`http://localhost:7000/restApi/grafo/random/` + numero_nodos);

	}

	else {
		alert(des_error);
	}
}



let getRequestAleatorio = (url) => {
	axios.get(url).then(response => {
		let grafo = response.data;
		console.log(grafo);
		setModel(grafo);
	}).catch(error => {
		console.log(error);
	});
}



/*Nivel 1-2
Funcion que se encarga de abrir un documento y procesarlo
*/

/*Nivel 1-3
Permite cerrar el espacio del grafo
*/

/*Nivel 1-4
Permite guardar el grafo en la base de datos

/*Nivel 1-5
Permite guardar el grafo como un JSON
*/

/*Nivel 1-6-1
Permite exportar los datos en un excel
*/

/*Nivel 1-6-2
Permite exportar los datos en una imagen
*/

/*Nivel 1-6-3
Permite exportar los datos en un PDF
*/

/*Nivel 1-7
Permite reinicializar el grafo




*/

/*----------Nivel 2-------*/

/*Nivel 2-1
Permite deshacer una accion
*/

/*--Nivel 2-2--
Nodos
*/

/*Nivel 2-2-1
Permite agegar un nodo
(Luego buscar si se especifica para crear nodos especificos)
*/
document.querySelector("#boton_crear_nodo").addEventListener("click", () => {
	crea_nuevo_nodo();
});

function crea_nuevo_nodo() {
	let nombre_nodo = document.querySelector('#nombre_nodo_nuevo').value;
	let error = false;
	let des_error = '';

	/*Se comprueba si el nombre es valido */
	if (Object.keys(nombre_nodo).length === 0 || Object.keys(nombre_nodo).length >= 30) {
		error = true;
		des_error = des_error + 'Error en el tamaño del nombre'
	}

	/*Se crea un nuevo nodo */
	if (error == false) {
		myDiagram.model.addNodeData({ t: nombre_nodo, color: "lightblue" });
	}

	else {
		alert(des_error);
	}

}

/*Nivel 2-2-2
Permite editar un nodo

/*Se debe seleccionar un solo nodo */
document.querySelector("#boton_editar_nodo").addEventListener("click", () => {
	edita_nodo();
});

function edita_nodo() {
	let nombre_nodo = document.querySelector('#nombre_nodo_edicion').value;
	let array_nodos = myDiagram.selection.toArray();

	/*Se revisa que el array tenga una sola posicion y sea un nodo */
	if (array_nodos.length === 1) {
		/*El array de nodo devuelve toda la informacion de cada nodo seleccionado, para nuestro uso solo se usara
        la kb que da la key y el nombre */
		let key = array_nodos[0]['kb']['key']


		/*Se busca el nodo para modificarlo */
		var data = myDiagram.model.findNodeDataForKey(key);
		if (data) {
			myDiagram.model.startTransaction("modified property");
			myDiagram.model.set(data, "t", nombre_nodo);
			myDiagram.model.commitTransaction("modified property");
		}
	}

	else {
		alert('Solo se pueden selecionar un nodo para modificar')
	}

}


/*Nivel 2-2-3
Permite eliminar un nodo
*/

function eliminar_nodo() {
	let array_nodos =[];


	
	/*El array de aristas devuelve todas las aristas seleccionadas*/

	myDiagram.selection.each(function(part) {
		console.log(part)
		console.log(go.Node)
		if (part instanceof go.Node) {
			if (part !== null) {
				array_nodos.unshift(part)
			}
			
		}
	})
	console.log(array_nodos);
	
	/*Se borran las aristas */
	array_nodos.forEach(element => {
		myDiagram.startTransaction();
		myDiagram.remove(element);
		myDiagram.commitTransaction("deleted node");

	});
	


}

/* function eliminar_nodo() {
	let array_nodos = myDiagram.selection.toArray();
	

	El array de nodo devuelve toda la informacion de cada nodo seleccionado, para nuestro uso solo se usara
	la kb que da la key y el nombre 
	for (let array of array_nodos) {
		let key = array['kb']['key']
		

		Por cada nodo seleccionado se busca por la key para borrarlo
		var node = myDiagram.findNodeForKey(key);
		if (node !== null) {
			myDiagram.startTransaction();
			myDiagram.remove(node);
			myDiagram.commitTransaction("deleted node");
		}
	}
}
 */

/*Nivel 2-3
Arco
*/

/*Nivel 2-3-1
Permite agregar un arco
*/

document.querySelector("#boton_crear_arco").addEventListener("click", () => {
	crea_arco();
});

function crea_arco() {
	let peso_arco = document.querySelector('#peso_arco').value;
	let array_nodos = myDiagram.selection.toArray();

	/*Se revisa que el array tenga dos nodos para ser conectados */
	if (array_nodos.length === 2) {
		/*El array de nodo devuelve toda la informacion de cada nodo seleccionado, para nuestro uso solo se usara
        la kb que da la key y el nombre */
		let inicio = array_nodos[0]['kb']['key']
		let fin = array_nodos[1]['kb']['key']
		let key_a=''

		/*Se concatenan los tres datos para formar la llave */
		key_a=key_a.concat(inicio,'_',fin,'_',peso_arco) 


		myDiagram.model.addLinkData({ from: inicio, to: fin, text:peso_arco,key:key_a});
	}

	else {
		alert('Solo se pueden selecionar dos nodo para modificar')
	}

}

/*Nivel 2-3-2
Permite editar un arco
*/







/*Nivel 2-3-3
Permite eliminar un arco
*/
function eliminar_arista() {
	let array_aristas =[];
	

	/*El array de aristas devuelve todas las aristas seleccionadas*/

	myDiagram.selection.each(function(part) {
		if (part instanceof go.Link) {
			if (part !== null) {
				array_aristas.unshift(part)
			}
			
		}
	})
	
	/*Se borran las aristas */
	array_aristas.forEach(element => {
		myDiagram.startTransaction();
		myDiagram.remove(element);
		myDiagram.commitTransaction("deleted node");

	});
	


}


/*----------Nivel 3-------*/

/*Nivel 3-1
Algoritmo
*/

/*Nivel 3-1-1
Algoritmo 1
*/

/*Nivel 3-1-2
Algoritmo 2
*/

/*Nivel 3-1-2n
Algoritmo 3
*/

/*----------Nivel 4-------*/

/*Nivel 4-1
Permite la ejecucion de la aplicacion del menu de aplicaciones
*/


/*----------Nivel 5 aplicaciones-------*/

/*Nivel 5-1
Aplicacion 1
*/

/*Nivel 5-2
Aplicacion 2
*/

/*Nivel 5-3
Aplicacion m
*/

/*----------Nivel 6 ventana-------*/

/*Nivel 5-1
Permite ver el modo grafico
*/

/*Nivel 5-2
Permite ver el modo tabla
*/

/*----------Nivel 6 ayuda-------*/

/*Nivel 5-1
Muestra ayuda
*/

/*Nivel 5-2
Muestra informacion sobre la aplicacion
*/


















