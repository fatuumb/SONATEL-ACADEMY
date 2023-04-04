const notificationContainer = document.querySelector(".principale");

// Fonction pour générer une notification avec la couleur donnée
function generateNotification(color) {
  const notification = document.createElement("div");
  notification.classList.add("principale", color);
  notificationContainer.appendChild(notification);
  setTimeout(function() {
    notificationContainer.removeChild(notification);
  }, 1000);
}

// Fonction pour ajouter un événement de clic sur chaque bouton
function addButtonEventListener(button, color) {
  bnt.addEventListener("click", function() {
    generateNotification(color);
  });
}

// Ajouter un événement de clic sur chaque bouton
addButtonEventListener(document.getElementById("vert"), "vert");
addButtonEventListener(document.getElementById("blue"), "blue");
addButtonEventListener(document.getElementById("rouge"), "rouge");
addButtonEventListener(document.getElementById("jaune"), "rouge");

