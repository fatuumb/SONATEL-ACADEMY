const lesElements={
  prof: [
      {nom: "Enseignant",cle:1},
      {nom: "Aly",cle:2},
      {nom: "Mbaye",cle:3},
      {nom: "Diallo",cle:4},
      {nom: "Djiby",cle:5},
      {nom: "Sow",cle:6},
      {nom: "Diop",cle:7}
      ],
  classe:[
      {nom: "Classe",effectif:null},
      {nom: "IAGE",capacite:20},
      {nom: "GDA",capacite:30},
      {nom: "RESEAU",capacite:40},
      {nom: "RI",capacite:50},
      {nom: "GL",capacite:60}
      ],

  matieres:[
      {nom: "Modules",cle:null},
      {nom: "Python",cle:2},
      {nom: "Langage C",cle:3},
      {nom: "javaScript",cle:4},
      {nom: "HTML",cle:5}
      ],  
  bureau:[
      {nom: "Salles",capacite:null},
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
  //   console.log(selectionner)
     
      //methode de mouhamed
  //   enseignant.addEventListener("click",function(){
  //     selectionner.innerHTML=""
  //     lesElements.prof.forEach(listE=>{
  //         const option=document.createElement("option")
  //         option.textContent=listE.nom
  //         selectionner.appendChild(option)
  //     })})

  //     classe.addEventListener("click",function(){
  //         selectionner.innerHTML=""
  //         lesElements.Classe.forEach(listC=>{
  //             const option=document.createElement("option")
  //             option.textContent=listC.nom
  //             selectionner.appendChild(option)
  //         })})

  //     modules.addEventListener("click",function(){
  //         selectionner.innerHTML=""
  //         lesElements.matieres.forEach(listM=>{
  //             const option=document.createElement("option")
  //             option.textContent=listM.nom
  //             selectionner.appendChild(option)
  //         })})

//fonction initial que je doit modifier
//+++++++++++++++++++++++++++++++++++++++++
      // function chargementdonnees(param){
      //     selectionner.innerHTML=""
      //     lesElements.param.forEach(listM=>{
      //         const option=document.createElement("option")
      //         option.textContent=listM.nom
      //         selectionner.appendChild(option)
      //     })
      //     }
//+++++++++++++++++++++++++++++++++++++++++



      //fonction qui marche
      function chargementdonnees(matieres){
          console.log(matieres);
          selectionner.innerHTML=""
          lesElements.matieres.forEach(listM=>{
              const option=document.createElement("option")
              option.textContent=listM.nom
              selectionner.appendChild(option)
          })
          }



          



