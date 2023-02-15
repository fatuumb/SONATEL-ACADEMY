#verification si le numero commence par lettre Maj
def testUpper(numero):
    if numero.isupper():
        return True
    else:
        return False

#verification de la taille du numero
def testTaille(numero,taille):
    if len(numero)>=taille:
        return True
    else:
        return False  
# n1="Numero1"
# n2=n1.upper()
# n2=0
# n3=0
n=0
testliste=[]
for i in testliste:
    print("--------")
    print(i)
    print(testUpper(i))
    print(testTaille(i,7))



#test si prenom commence par lettre 
def testPremierAlpha(chaine):
  if chaine[0].isalpha():
      return True
  else:
      return False



#####
# def testTaille(numero,taille):
#     if len(numero)>=taille:
#         return True
#     else:
#         return False



#test si taille =3
def testPrenom(prenom):
  if testPremierAlpha(prenom) & testTaille(prenom,3):
    return True
  else:
    return False

# p1="Modou"
# p2="2Amadou"
# p3="Ba"

testliste=[]
for i in testliste:
    print("--------")
    print(i)
    print(testPremierAlpha(i))
    # print(len(i))
    print(testTaille(i,3))
    print("--------")



#test si prenom commence par lettre 
def testPremierAlpha(chaine):
  if chaine[0].isalpha():
      return True
  else:
      return False



#test si taille =3
def testNom(nom):
  if testPremierAlpha(nom) & testTaille(nom,2):
    return True
  else:
    return False

# d1="21/10/04"
# d2="05/mars/2002"
# d3="25_11_2004"
# d4="12 03 1999"
# d5="30.02.2023"

listeDate=[]
import datetime


#separateur de date
def sepDate(chaine):
  chaine = chaine.replace('mars', '03').replace('.', '/').replace('-', '/').replace('_', '/').replace(' ', '/')
  return chaine


#verification de la date 
def dateCorrecte(aa,mm,jour):
  try:
      newDate = datetime.datetime(int(aa),int(mm),int(jour))
      correctDate = True
  except ValueError:
      correctDate = False
  return correctDate

for i in listeDate:
  i=sepDate(i)
  i=i.split("/")
  print(i)
  print(dateCorrecte(int(i[2]),int(i[1]),int(i[0])))

# def testdate(date):
#   if
# c1="4eC"
# c2="4enE"
# c4="5emc"
# c3="2ndB"

#test de la validation de la classe
def classeValide(chaine):
  if chaine[0] in ["3","4","5","6"] and chaine[-1].upper() in ["A","B","C","D"]:
    # print(chaine[0]," eme ",chaine[-1].upper())
    # print("C bon")
    return True
  else:
    # print('Pas bon')
    return False

for i in []:
  print("----------")
  print(i,classeValide(i))
  classeValide(i)

n1=0
n2=0
listeNotes=[n1,n2]


for note in listeNotes:
  #Separation des matiere par des "#"
  note=note.split("#")
  dic={}
  for matiere in note:
    # separer nom et valeur notes
    matiere=matiere.split('[')
    
    nom=matiere[0]
    dic[nom]=matiere[1]
  print(dic)
  matiere=dic
  for i in matiere:
    matiere[i]=matiere[i].split(':')

    # print(matiere[i])
    matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
    matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
    matiere[i]["examen"]=matiere[i]["examen"].replace("]","")
    note=matiere

    # for i in matiere:
    #   print(i)
    # print(matiere[i])
matiere[i]=matiere[i]
# matiere[i]=matiere[i].split(':')
      
matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
matiere[i]["examen"]=matiere[i]["examen"].replace("]","")

matiere = {
#   "Francais": '4|11:13]',
#   "Anglais": "13,5:15]",
#   "PC": '11:9]'
}
print(matiere)
for i in matiere:
  # print(i)
  # print(matiere[i])

  matiere[i]=matiere[i].split(':')
  
  # print(matiere[i])
  matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
  matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
  matiere[i]["examen"]=matiere[i]["examen"].replace("]","")

matiere
listeNotes



































# def testUpper(numero):
#     if numero.isupper():
#         return True
#     else:
#         return False

# def testTaille(numero,taille):
#     if len(numero)>=taille:
#         return True
#     else:
#         return False
    

# n1="Numero1"
# # n2=n1.upper()
# n2="NUMERO2"
# n3="ABC123"
# testliste=[n1,n2,n3]
# for i in testliste:
#     print("--------")
#     print(i)
#     print(testUpper(i))
#     print(testTaille(i,7))



# def testPremierAlpha(chaine):
#   if chaine[0].isalpha():
#       return True
#   else:
#       return False

# def testTaille(numero,taille):
#     if len(numero)>=taille:
#         return True
#     else:
#         return False

# def testPrenom(prenom):
#   if testPremierAlpha(prenom) & testTaille(prenom,3):
#     return True
#   else:
#     return False

# p1="Modou"
# p2="2Amadou"
# p3="Ba"

# testliste=[p1,p2,p3]
# for i in testliste:
#     print("--------")
#     print(i)
#     print(testPremierAlpha(i))
#     # print(len(i))
#     print(testTaille(i,3))
#     print("--------")



# def testPremierAlpha(chaine):
#   if chaine[0].isalpha():
#       return True
#   else:
#       return False


# def testNom(nom):
#   if testPremierAlpha(nom) & testTaille(nom,2):
#     return True
#   else:
#     return False




# d1="21/10/04"
# d2="05/mars/2002"
# d3="25_11_2004"
# d4="12 03 1999"
# d5="30.02.2023"

# listeDate=[d1,d2,d3,d4,d5]
# import datetime

# def sepDate(chaine):
#   chaine = chaine.replace('mars', '03').replace('.', '/').replace('-', '/').replace('_', '/').replace(' ', '/')
#   return chaine

# def dateCorrecte(aa,mm,jour):
#   try:
#       newDate = datetime.datetime(int(aa),int(mm),int(jour))
#       correctDate = True
#   except ValueError:
#       correctDate = False
#   return correctDate


# for i in listeDate:
#   i=sepDate(i)
#   i=i.split("/")
#   print(i)
#   print(dateCorrecte(int(i[2]),int(i[1]),int(i[0])))




# # def testdate(date):
# #   if 



# c1="4eC"
# c2="4enE"
# c4="5emc"
# c3="2ndB"



# def classeValide(chaine):
#   if chaine[0] in ["3","4","5","6"] and chaine[-1].upper() in ["A","B","C","D"]:
#     # print(chaine[0]," eme ",chaine[-1].upper())
#     # print("C bon")
#     return True
#   else:
#     # print('Pas bon')
#     return False

# for i in [c1,c2,c4,c3]:
#   print("----------")
#   print(i,classeValide(i))
#   classeValide(i)



# n1="Francais[4|11:13]#Anglais[13,5:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]#Math[12|14,5|11:13]"
# n2="Math[12|11:13]#Francais[4|11|8:13]#Anglais[13,5|11:15]#PC[11:9]#SVT[12|9|16|11:12]#HG[10:13]"
# listeNotes=[n1,n2]




# for note in listeNotes:
#   #Separation des matiere par des "#"
#   note=note.split("#")
#   dic={}
#   for matiere in note:
#     # separer nom et valeur notes
#     matiere=matiere.split('[')
    
#     nom=matiere[0]
#     dic[nom]=matiere[1]
#   print(dic)
#   matiere=dic
#   for i in matiere:
#     matiere[i]=matiere[i].split(':')

#     # print(matiere[i])
#     matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
#     matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
#     matiere[i]["examen"]=matiere[i]["examen"].replace("]","")
#   note=matiere

  
#     # for i in matiere:
#     #   print(i)
#     # print(matiere[i])
# matiere[i]=matiere[i]
# matiere[i]=matiere[i].split(':')
      
# matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
# matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
# matiere[i]["examen"]=matiere[i]["examen"].replace("]","")

# matiere = {
#   "Francais": '4|11:13]',
#   "Anglais": "13,5:15]",
#   "PC": '11:9]'
# }
# print(matiere)
# for i in matiere:
#   # print(i)
#   # print(matiere[i])

#   matiere[i]=matiere[i].split(':')
  
#   # print(matiere[i])
#   matiere[i]={"devoirs":matiere[i][0],"examen":matiere[i][1]}
#   matiere[i]["devoirs"]=matiere[i]["devoirs"].split("|")
#   matiere[i]["examen"]=matiere[i]["examen"].replace("]","")

# matiere
# listeNotes