/* 
Benjamin Oertel
J'aimerais que tu developes un programme javascript (pure js, pas de framework) qui permette de trouver le td qui contient un X
*/

// Pour choisir la bonne manière de faire : changer le numéro dans le switch
function findX() {
	switch(1) {
		case 1:
		tds();
		break;
		
		case 2:
		table();
		break;
		
		case 3:
		mix();
		break;
		
		case 4:
		querySelector();
		break;
		
		case 5:
		arbre(document);
		break;
	}
}

/*
#5 : En parcourant à l'arbre de la page web
+ : En parcourant l'arbre, on peut facilement le modifier (appendChild, removeChild)
- : pas très compréhensible
*/
function arbre(element) {
    for (var i= 0, n=element.childNodes.length; i<n; i++) {
        var child = element.childNodes[i];
        if (child.nodeType === 1) {
        	// on recherche le TD et xFound va tester le contenu de ce td.
            if (child.tagName === "TD" && xFound(child, 5)) {}	// nodeType = 1 : noeud; (2 = attribut;  3 = feuille)
			else {
	            arbre(child);
            }
        }

    }
}
/*
#4 : Utilisation de querySelectorAll
+ : dans ce cas, pas tellement plus d'avantage que getElementsByTagName mais le selector est plus puissant (selection en fonction des attributes des éléments)
- : ne pas oublier le <tbody> qui est ajouté par le navigateur.
*/
function querySelector() {
	var tds = document.querySelectorAll("table > tbody > tr > td");
	for (i = 0; i<tds.length; i++) {
		xFound(tds[i], 4);
	}
}

/*
#3 : mix de la solution 1 en parcourant les td que du premier tableau.
Solution #1 mais parcours 
*/
function mix() {
	var table = document.getElementsByTagName("table")[0];
	var tds = table.getElementsByTagName("td");
	
	for (i = 0; i<tds.length; i++) {
		xFound(tds[i], 3);
	}
}

/*
#2 : Parcours de chaque cellule du premier tableau de la page
+ : passage par tous les éléments du tableau ( = inconvénient)
- : double boucle, long en temps d'éxécution.
*/
function table() {
	var arrays = document.getElementsByTagName("table");
	var rows = arrays[0].rows;

	for(i=0; i<rows.length; i++) {
		var cols = rows[i].cells;

		for (j=0; j<cols.length; j++) {
			xFound(cols[j], 2);
		}
	}
}

/* 
#1 : On regarde le contenu de tous les éléments <td>
+ : très simple d'utilisation
- : selection de tous les td de la page. Embetant s'il y a plusieurs tableaux dans la page et qu'on doit faire la recherche que sur un seul.
*/
function tds() {
	var tds = document.getElementsByTagName("td");
	for(i=0; i<tds.length; i++) {
		xFound(tds[i], 1);
	}
}


// Fonction qui teste le contenu de l'élément et affiche une alerte et colorie la cellule en rouge.
function xFound(element, method) {
	// textContent : pour les navigateurs respectant le standard, innerText pour les autres (=IE < 9)
	// === dépend du type de expressions testées.
	if (element.textContent === "X" || element.innerText === "X") {
		alert("I found X [" + method + "]");
		element.style.backgroundColor = "#FF0000";
		return true;
	}
	else {
		return false;
	}
}
