#Écrire un programme qui permet de saisir une phrase. Le programme enlève tous les espaces
#inutiles de la phrase.
phrase=input("entrer une phrase:\n") 
def Separateur(phrase):
  ch=""
  ajout_espace=False
  for char in phrase:   
    if char ==" ":
       if not ajout_espace:
        ch+=char
        ajout_espace=True
    
    else:
        ch+=char
        ajout_espace=False
  return (ch)
var=Separateur(phrase)
print(var)
