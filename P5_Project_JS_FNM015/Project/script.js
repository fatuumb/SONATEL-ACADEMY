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
        {nom: "HTML",cle:5},
        {nom: "sql",cle:5}

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
                const span =document.querySelector(".recup")
                span.textContent=recuperer.textContent
                if (recuperer.textContent=="Aly") {
                    remplisage(obj1)
                }

            })
        }
const prof = document.querySelector("#Enseignants")
prof.addEventListener('click',function(){
    chargementdonnees("Enseignant")
    recuplabel()
})
        const obj1 = { name: "Aly",jour: 'lundi',salles:'A1',modules:'langage c',heure:'08h-10H',classe:'IAGE'};
        const obj2 = { name: "Mbaye", jour: 'mardi',salles:'B1',modules:'python',heure:'10H-11H',classe:'GDA' };
        const obj3 = { name: "diallo", jour: 'mercredi',salles:'B1',modules:'javaScript',heure:'12H-13H',classe:'IAGE' };
        const obj4 = { name: "Sow", jour: 'lundi',salles:'C3',modules:'html',heure:'14h-15h',classe:'RESEAU' };
        const obj5 = { name: "Diop", jour: 'lundi',salles:'D4',modules:'sql',heure:'16-17H',classe:'RI'};
        objectsList = [obj1, obj2, obj3, obj4,obj5];

        objectsList.forEach((obj) => {
        //    remplisage(`Name: ${obj.name}, jour: ${obj.jour},salles: ${obj.salles},modules: ${obj.modules},heure: ${obj.heure}`);
          remplisage(obj)
    });
          
          function remplisage(obj){
            const nouveauDiv =document.createElement ('div')
            const p1 =document.createElement('p')
            const p2 =document.createElement('p')
            const p3 =document.createElement('p')

            nouveauDiv.classList.add("newDiv")

            p1.textContent=obj.classe
            p2.textContent=obj.modules
            p3.textContent=obj.salles

            nouveauDiv.appendChild(p1);
            nouveauDiv.appendChild(p2);
            nouveauDiv.appendChild(p3);


            let jours = document.querySelector('#monday')
            console.log(jours)

            // if (obj.jour=='lundi') {
            //     jours = document.querySelector('#monday')
            // }
            // if (obj.jour=='mardi') {
            //     jours=document.querySelector('#thuesday')
            // }
            console.log(jours)
            jours.appendChild (nouveauDiv)
          }







        
            


            

  

