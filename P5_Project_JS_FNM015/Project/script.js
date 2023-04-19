// // Récupérer le bouton de mode
// var modeBtn = document.getElementById('toggle');
// // Vérifier si le mode est défini sur "sombre" dans le stockage local (localStorage)
// if (localStorage.getItem('mode') === 'sombre') {
//   // Activer le mode sombre
//   activerModeSombre();
// }

// // Ajouter un écouteur d'événement "clic" au bouton de mode
// modeBtn.addEventListener('click', function() {
//     // Vérifier si le mode est actuellement "clair"
//     if (document.body.classList.contains('mode-clair')) {
//       // Activer le mode sombre
//       activerModeSombre();
//     } else {
//       // Activer le mode clair
//       activerModeClair();
//     }
//   });
// // Fonction pour activer le mode sombre
// function activerModeSombre() {
//     // Ajouter la classe "mode-sombre" au corps de la page
//     document.body.classList.add('mode-sombre','bg-dark');
//     document.getElementById("sidebarMenu").classList.add('bg-dark')
//     document.getElementById("navbar").classList.add('bg-dark',)
//     document.getElementById("aly").classList.add('text-light')
  
//     // Supprimer la classe "mode-clair" du corps de la page
//     document.body.classList.remove('mode-clair');
//     document.getElementById("sidebarMenu").classList.remove('bg-dark-subtle')
//     document.getElementById("navbar").classList.remove('bg-light', "text-dark")
//     document.getElementById("aly").classList.remove('text-dark')
  
//     // Mettre à jour le texte du bouton de mode
//     modeBtn.innerHTML = 'Mode clair';
//     // Enregistrer le mode actuel dans le stockage local (localStorage)
//     localStorage.setItem('mode', 'sombre');
//   }
//   // Fonction pour activer le mode clair
//   function activerModeClair() {
//     // Ajouter la classe "mode-clair" au corps de la page
//     document.body.classList.add('mode-clair', 'bg-light');
//     document.getElementById("sidebarMenu").classList.add('bg-light')
//     document.getElementById("navbar").classList.add('bg-light')
//     document.getElementById("aly").classList.add('text-dark')
  
//     // Supprimer la classe "mode-sombre" du corps de la page
//     document.body.classList.remove('mode-sombre', 'bg-dark');
//     document.getElementById("sidebarMenu").classList.remove('bg-dark')
//     document.getElementById("navbar").classList.remove('bg-dark')
//     document.getElementById("aly").classList.remove('text-light')
  
//     // Mettre à jour le texte du bouton de mode
//     modeBtn.innerHTML = 'Mode sombre';
//     // Enregistrer le mode actuel dans le stockage local (localStorage)
//     localStorage.setItem('mode', 'clair');
//   }




const enseignant=document.getElementById("Enseignants")
const salles=document.getElementById("Salle")
const classe=document.getElementById("Classes")
const modules=document.getElementById("Modules")
const selectionner =document.querySelector(".form-select")
const iconPlus=document.querySelectorAll('#icons')

const lundi = document.querySelector('#monday')
const mardi = document.querySelector('#thuesday')
const mercredi = document.querySelector('#merc')
const jeudi = document.querySelector('#jen')

const obj1 = { name: "Aly",jour: 'lundi',salles:'A1',modules:'langage c',heureDebut:'08h',heureFin:'10H',classe:'IAGE'};
const obj2 = { name: "Mbaye", jour: 'mardi',salles:'B1',modules:'python',heureDebut:'10h',heureFin:'11H',classe:'GDA' };
const obj3 = { name: "Diallo", jour: 'mercredi',salles:'B1',modules:'javaScript',heureDebut:'12h',heureFin:'13H',classe:'IAGE' };
const obj4 = { name: "Djiby", jour: 'jeudi',salles:'C3',modules:'html',heureDebut:'14h',heureFin:'15H',classe:'RESEAU' };
objectsList = [obj1, obj2, obj3, obj4];

const lesElements={
    Enseignant: [
        {nom: "Enseignant",cle:1,module:[null]},
        {nom: "Aly",cle:2,module:["langage c","python"]},
        {nom: "Mbaye",cle:3,module:["javaScript"]},
        {nom: "Diallo",cle:4,module:["HTML"]},
        {nom: "Djiby",cle:5,module:["sql"]}
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
    //   selectionner.textContent="Enseignant"
    //   selectionner.textContent="Classes"

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
    }
  )

selectionner.addEventListener('change',function(){
 
    if (selectionner.value==obj2.name) {
        remplisage(obj2)

    }
    if (selectionner.value==obj3.name) {
        remplisage(obj3)

    } 
    if (selectionner.value==obj4.name) {
        remplisage(obj4)
    }
  }
) 

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

    if (obj.jour=='lundi') {
        lundi.appendChild(nouveauDiv)
    }

    if (obj.jour=='mardi') {
        mardi.appendChild(nouveauDiv)
    }

    if (obj.jour=='mercredi') {
        mercredi.appendChild(nouveauDiv)
    }

    if (obj.jour=='jeudi') {
        mercredi.appendChild(nouveauDiv)
    }
  }
  const form =document.querySelector('.formulaire')

  function ajouterEnseignant() {
    const formu= document.createElement('form')
    const p =document.createElement('p')
    const div1 =document.createElement('div')
    const div2 =document.createElement('div')
    const div3 =document.createElement('div')
    const label1=document.createElement('label')
    const label2=document.createElement('label')
    const label3=document.createElement('label')
    const input1 =document.createElement('input')
    const input2 =document.createElement('input')
    const input3 =document.createElement('input')
    
    p.textContent="Ajouter"
    label1.textContent="Nom"
    label2.textContent="Identifiant"
    label3.textContent="Module"

    


    div1.appendChild(label1);
    div1.appendChild(input1);

    div2.appendChild(label2);
    div2.appendChild(input2);

    div3.appendChild(label3);
    div3.appendChild(input3);

   





  }




  iconPlus.forEach(element => {
    element.addEventListener('click',function() {
        form.style.display="block"
    
        
    })
    
});


const an =document.querySelector("#anuller")
    an.addEventListener('click',function () {
        form.style.display="none"
        
    })

    