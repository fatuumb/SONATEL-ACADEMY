    var compteur = 0; // variable pour garder une trace du nombre de composants créés

    // fonction pour ajouter un nouveau composant
    function ajouterComposant() {
        compteur++; // incrémenter le compteur

        // créer un nouveau div pour le composant
        var divComposant = document.createElement("div");
        divComposant.id = "composant_" + compteur;
        divComposant.className = "composant";

        // créer un textarea pour le composant
        var textareaComposant = document.createElement("textarea");
        textareaComposant.id = "textarea_" + compteur;
        textareaComposant.className = "textarea";
        divComposant.appendChild(textareaComposant);

        // créer une icône "edit" pour le composant
        var iconeEdit = document.createElement("i");
        iconeEdit.className = "fa fa-edit";
        iconeEdit.onclick = function() {
            if (textareaComposant.disabled) {
                textareaComposant.disabled = false;
            } else {
                textareaComposant.disabled = true;
            }
        };
        divComposant.appendChild(iconeEdit);

        // créer une icône "corbeille" pour le composant
        var iconeCorbeille = document.createElement("i");
        iconeCorbeille.className = "fa fa-trash";
        iconeCorbeille.onclick = function() {
            divComposant.remove();
        };
        divComposant.appendChild(iconeCorbeille);

        // ajouter le nouveau composant à la page
        document.getElementById("liste_composants").appendChild(divComposant);
    }
