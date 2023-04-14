const lesElements={
    Enseignant: [
        {nom: "Enseignant",cle:1},
        {nom: "Aly",cle:2},
        {nom: "Mbaye",cle:3},
        {nom: "Diallo",cle:4},
        {nom: "Djiby",cle:5},
        {nom: "Sow",cle:6},
        {nom: "Diop",cle:7}
        ],
    classe:[
        {nom: "classe",effectif:null},
        {nom: "IAGE",capacite:20},
        {nom: "GDA",capacite:30},
        {nom: "RESEAU",capacite:40},
        {nom: "RI",capacite:50},
        {nom: "GL",capacite:60}
        ],

    module:[
        {nom: "module",cle:null},
        {nom: "Python",cle:2},
        {nom: "Langage C",cle:3},
        {nom: "javaScript",cle:4},
        {nom: "HTML",cle:5}
        ],  
    salle:[
        {nom: "salles",capacite:null},
        {nom: "A1",capacite:40},
        {nom: "B2",capacite:50},
        {nom: "C3",capacite:56},
        {nom: "D4",capacite:74},
        {nom: "E5",capacite:80},

        ]
      }
      const enseignant=document.getElementById("Enseignants")
      const salles=document.getElementById("Salle")
      const classe=document.getElementById("Classes")
      const modules=document.getElementById("Modules")
      const selectionner =document.querySelector(".form-select")
      selectionner.textContent="Enseignant"
      selectionner.textContent="Classes"

        function chargementdonnees(param){
            const  table =["Enseignant","salle","classe","module"];
            table.forEach(elem=>{
                    if (param==elem){
                        selectionner.innerHTML=""
                        lesElements[param].forEach(listM=>{
                    const option=document.createElement("option")
                    option.textContent=listM.nom
                    selectionner.appendChild(option)
                    option.addEventListener ("click",recuplabel()) 
                })}})}
                
        function recuplabel() {
            const selectionner =document.querySelector(".form-select")
            selectionner.addEventListener('change',function(){
                const recuperer=this.options[this.selectedIndex]
                console.log(recuperer);
                const span =document.querySelector(".recup")
                span.textContent=recuperer.textContent
                console.log(recuperer);
            })
        }

        







        
            


            

  

