function createBox() {
	// Création d'une nouvelle div pour la fenêtre
	var div = document.createElement("div");
	div.className = "box";
	div.innerHTML = "Fenêtre " + (document.getElementsByClassName("box").length + 1);

	// Ajout de la div au conteneur
	document.getElementById("container").appendChild(div);

	// Ajout d'un gestionnaire d'événements pour la suppression de la fenêtre
	div.onclick = function() {
		this.parentNode.removeChild(this);
	};
}
