# Écrire un programme qui permet de saisir une chaîne de N phrases. Le programme enlève
# tous les espaces inutiles de chaque phrase puis réaffiche les phrases corrigées.
# Règles de Gestion
# ● La chaîne de saisie est Obligatoire
# ● Les phrases ne doivent pas contenir des caractères spéciaux
# ● Une phrase commence par une lettre majuscule et se termine par un point (. ou ?ou !)
# ● Chaque phrase contiendra au moins 25 caractères


ch=""
phrs=input("entrer une chaine:\n") 
while phrs!="A" : #and phrs==['A-Za-z.']  
 def Separateur(phrase):
    texte = ""
    for i in range (len(texte)):
      if i < len(phrase) -1 and phrase == " " and phrase[i+1] == " ":
        continue
      else:
        texte+= texte[i]
    return texte

 def unaun(phrase):
    ch=[]
    lesphrase= ""
    for i in range (len(lesphrase)):
        if phrase[i] in ['A-Za-z.']:
            for j in range (i,len(phrase)):
                lesphrase += lesphrase[j]
                if lesphrase[j] in ['?','.',',','!']:
                    if len (lesphrase)>=25:
                        ch.append(lesphrase)
                        lesphrase=""
                        break

  #   ajout_espace=False
  #   for char in phrase:   
  #     if char ==" ":
  #       if not ajout_espace:
  #         ch+=char
  #         ajout_espace=True
      
  #     else:
  #         ch+=char
  #         ajout_espace=False
  #   return (ch)
  # var=Separateur(phrase)
  # print(var)


#le prof
# def retourn_chaine():
# chaine=""
# chaine=input("entrer une chaine:\n"):



















# phrase=input("entrer une phrase:\n")
# while phrase!=" " and phrase==['A-Za-z.']:
#   def Separateur(phrase):
#     ch=" "
#     ajout_espace=False
#     for char in phrase:   
#       if char ==" ":
#         if not ajout_espace:
#           ch+=char
#           ajout_espace=True
      
#       else:
#           ch+=char
#           ajout_espace=False
#       print(ch)
#     return (ch)
#   var=Separateur(phrase)
#   print(var)
