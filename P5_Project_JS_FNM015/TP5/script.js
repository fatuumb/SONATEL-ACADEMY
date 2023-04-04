// Définition du tableau de questions
const questions = [
    {
      question: "Quel est le nom de la capitale du Japon?",
      options: ["Kyoto", "Tokyo", "Osaka", "Hiroshima"],
      answer: "Tokyo"
    },
    {
      question: "Quel est le plus grand océan du monde?",
      options: ["Atlantique", "Pacifique", "Arctique", "Indien"],
      answer: "Pacifique"
    },
    {
      question: "Quel est l'animal le plus rapide sur Terre?",
      options: ["Le guépard", "Le lion", "Le léopard", "La panthère"],
      answer: "Le guépard"
    },
    {
      question: "Combien de continents y a-t-il dans le monde?",
      options: ["5", "6", "7", "8"],
      answer: "7"
    },
    {
      question: "Quel est l'élément chimique représenté par le symbole H?",
      options: ["Hydrogène", "Hélium", "Azote", "Oxygène"],
      answer: "Hydrogène"
    }
  ];
  
  // Initialisation des variables
  let currentQuestion = 0;
  let score = 0;
  
  // Sélection des éléments HTML
  const questionText = document.getElementById("question-text");
  const optionsContainer = document.getElementById("options-container");
  const scoreText = document.getElementById("score-text");
  const nextButton = document.getElementById("next-button");
  
  // Fonction pour afficher une question
  function displayQuestion() {
    const current = questions[currentQuestion];
    questionText.textContent = current.question;
    optionsContainer.innerHTML = "";
    current.options.forEach((option) => {
      const button = document.createElement("button");
      button.textContent = option;
      button.addEventListener("click", () => {
        if (button.textContent === current.answer) {
          score++;
          scoreText.textContent = `Score: ${score}`;
        }
        nextButton.disabled = false;
        button.disabled = true;
      });
      optionsContainer.appendChild(button);
    });
  }
  
  // Affichage de la première question
  displayQuestion();
  
  // Gestionnaire d'événements pour le bouton Suivant
  nextButton.addEventListener("click", () => {
    currentQuestion++;
    if (currentQuestion === questions.length) {
      questionText.textContent = `Votre score final est ${score} sur ${questions.length}!`;
      optionsContainer.innerHTML = "";
      nextButton.disabled = true;
    } else {
      displayQuestion();
      nextButton.disabled = true;
    }
  });
  