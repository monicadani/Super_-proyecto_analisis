let getRequest=(url)=>{
	axios.get(url).then(response => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(response.data)+"</pre>";
	}).catch(error => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(error)+"</pre>";
	});
}

let deleteRequest=(url)=>{
	axios.delete(url).then(response => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(response.data)+"</pre>";
	}).catch(error => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(error)+"</pre>";
	});
}

let postRequest=(url,data,options)=>{
	axios.post(url,data,options).then(response => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(response.data)+"</pre>";
	}).catch(error => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(error)+"</pre>";
	});
}

let putRequest=(url,data,options)=>{
	axios.put(url,data,options).then(response => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(response.data)+"</pre>";
	}).catch(error => {
		document.querySelector("#app").innerHTML = "<pre>"+prettyPrintJson.toHtml(error)+"</pre>";
	});
}

let request=(type,url,data)=>{
	document.querySelector("#app").innerHTML = "ESPERANDO RESPUESTA DEL SERVIDOR..."
	const options = {
		headers: {
			'X-Master-Key': '$2b$10$LhCbDpA5gOD3zUpsiCMNLOqpMALprhx4suc18LQUwiYgxYQPmJcgS',
			'Content-Type': 'application/json'
		}
	};
	switch (type) {
		case "GET":
			getRequest(url);
			break;
		case "PUT":
			putRequest(url,data,options);
			break;
		case "POST":
			postRequest(url,data,options);
			break;
		case "DELETE":
			deleteRequest(url);
			break;
		default:
			break;
	}
}




