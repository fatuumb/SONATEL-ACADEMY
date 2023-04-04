let monTableau = ["Mon Premier"," Mon Deuxième",
"Mon Troisième","Mon Quatrième"];

const gauche = document.querySelector('.left');

const  droite = document.querySelector('.right');

for (let index = 0; index < monTableau.length; index++) {
        let ph = document.createElement('p')
            ph.innerText = monTableau[index]
            gauche.appendChild(ph)
}
const p = document.querySelectorAll('p')
p.forEach(element => {
   element.addEventListener('click',()=>{
      console.log(element);
      element.classList.toggle('active')
   })
});

