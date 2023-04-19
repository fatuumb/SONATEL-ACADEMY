<h2>Formulaire en JavaScript</h2>

<form>
  <label for="nom">Nom:</label>
  <input type="text" id="nom" name="nom"><br>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email"><br>

  <label for="message">Message:</label>
  <textarea id="message" name="message"></textarea><br>

  <input type="submit" value="Envoyer" onclick="validerFormulaire()">
</form>

<script>
function validerFormulaire() {
  var nom = document.forms[0]["nom"].value;
  var email = document.forms[0]["email"].value;
  var message = document.forms[0]["message"].value;

  if (nom == "" || email == "" || message == "") {
    alert("Veuillez remplir tous les champs!");
    return false;
  }

  alert("Le formulaire a été envoyé avec succès!");
}
</script>

</body>
</html>