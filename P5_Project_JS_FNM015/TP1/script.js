    //ajout un element
        const bnt=document.querySelector('.bnt');
        bnt.addEventListener('click',ajouterComposant);

        function ajouterComposant(){
            let note = document.createElement('div')
            note.className = 'note'

            let header = document.createElement('div')
            header.className = 'header'

            const iconeCorbeille = document.createElement("i");
            iconeCorbeille.className = "fa fa-trash";
            
            const iconeEdit = document.createElement("i");
            iconeEdit.className = "fa fa-edit";
            iconeEdit.onclick = function() {
                if (textareaComposant.disabled) {
                    textareaComposant.disabled = false;
                } else {
                    textareaComposant.disabled = true;

                }
            };

            iconeCorbeille.className = "fa fa-trash";
            iconeCorbeille.onclick = function() {
             note.remove();};
            header.append(iconeEdit,iconeCorbeille)

            let body = document.createElement('div')
            body.className = 'body'

            const textareaComposant = document.createElement("textarea");
            body.appendChild(textareaComposant)
            note.append(header,body)
            console.log(note);

            let composant = document.getElementById('liste_composants')
composant.appendChild(note)
}





    

        
        


  


    

    