#creation de la classe
from csv import DictReader
from pprint import pprint
from datetime import datetime
import re


class Donnee:
#le constructeur
    def __init__(self,filename):
        self.filename = filename
 #retourne une liste de dictionnaire
    def recup_valeurs(self):
      valeurs =[]
      with open (self.filename,'r')as file:
         for line in DictReader(file):
            valeurs.append(line)
      return valeurs
filename='Project.csv'
data=Donnee(filename)
co=data.recup_valeurs()

# pprint(co)

class Etudiant:
    def __init__(self,info):
      self.info=info
      # self.CDE       = CODE
      # self.Nm        = Nom
      # self.Prnom     = Prénom
      # self.Num       = Numero
      # self.Nte       = Note
      # self.Clse      = Classe
      # self.nsance    = naissance

    def numeroValide(self):
        if len(self.info) == 7:
            if self.info.isalnum() == True:
                print(self.info)
                if self.info.isupper() == True:
                    if any(c.isdigit()for c in self.info) == True:
                        return True


Etudiant(co[2]["Numero"]).numeroValide()
#print(co[9])

# listeObject=[]
# for i in co:
#    etudiant=Etudiant(i["CODE"],i["Numero"],i["Nom"],i["Prénom"],i["Date de naissance"],i['Classe'],i['Note'])
#    listeObject.append(etudiant)
# for i in (listeObject):
#    print('\n\n')
#    print(vars(i))

# #      #verification des numeros 
# def numeroValide(self):
#         if len(self.Numeros) == 7:
#             if self.Numeros.isalnum() == True:
#                 print(self.Numeros)
#                 if self.Numeros.isupper() == True:
#                     if any(c.isdigit()for c in self.Numeros) == True:
#                         return True

# Etudiant.numeroValide(Etudiant)


#pprint(listeObject)

# def __str__(self):
#         return (f"{self.Nom}-{self.Prénom}")
#   def affiche_eleves(self):
#       print(f"""
#            Nom:{self.Nom} 
#            Prénom:{self.Prénom}
#            Numeros:{self.Numeros}  
#            Note:{self.Note}  
#            Classe:{self.Classe}
#            Naissance:{self.Naissance}         
#            """)



# #      #verification des numeros 
# def numeroValide(self):
#         if len(self.Numeros) == 7:
#             if self.Numeros.isalnum() == True:
#                 print(self.Numeros)
#                 if self.Numeros.isupper() == True:
#                     if any(c.isdigit()for c in self.Numeros) == True:
#                         return True

# Etudiant.numeroValide(Etudiant)

#       #prenom
#   def prenomValide(self):
#         cnt = 1
#         if (self.Prénom == ""):
#             return False
#         elif self.Prénom[0] >= 'a' and self.Prénom[0] <= 'z' or self.Prénom[0] >= 'A' and self.Prénom[0] <= 'Z':
#             for i in range(1,len(prenom)):
#                 if self.Prénom[i] >= 'a' and self.Prénom[i] <= 'z' or self.Prénom[i] >= 'A' and self.Prénom[i] <= 'Z':
#                     cnt += 1
#             if cnt >= 3:
#                 return True
#             else:
#                 return False    
#         else:
#             return False 
        
#       #nom
#   def nomValide(self,nom):
#         nbre = 1
#         if (nom == ""):
#             return False
#         elif nom[0] >= 'a' and nom[0] <= 'z' or nom[0] >= 'A' and nom[0] <= 'Z':
#             for i in range(1,len(nom)):
#                 if nom[i] >= 'a' and nom[i] <= 'z' or nom[i] >= 'A' and nom[i] <= 'Z':
#                     nbre += 1
#             if nbre >= 2:
#                 return True 
#             else:
#                 return False
            
#         else:
#             return False  

#       #date
#   def changerFormatDate(self,date):
#         dateF =""
#         listeMois =["janvier","février","mars","avril","mai","juin","juillet","août","septembre","octobre","novembre","decembre"]
#         listeSep =[' ',',','-',';','_','/','.',':']
#         if date == "" or date == " ":
#             return False
#         else:    
#             for c in date:
#                 if c in listeSep:
#                     sep=c
#                     dateF = date.replace(sep,"-")     
#             dateL = dateF.split("-")
#             if len(dateL) == 3:
#                 for i  in range(len(listeMois) -  3):
#                     if listeMois[i] == dateL[1]:
#                         dateL[1] = "0"+str(i + 1)
#                 for j in  range(9,len(listeMois)):
#                     if listeMois[j] == dateL[1]:
#                         dateL[1] =str(j + 1)
#                 dateL = "-".join(dateL)
#                 for c in dateL:
#                     if c not in ["0","1","2","3","4","5","6","7","8","9","-"]:
#                         return False                       
#                 return dateL
#             else:
#                 return False

#   def dateValide(sef,date):
#         date = date.split("-")
#         jour = int(date[0])
#         mois = int(date[1])
#         annee = int(date[2])
#         try:
#             date = datetime.datetime(annee,mois,jour).strftime("%d-%m-%y")
#         except:
#             return False
#         return True             

#       #classe
#   def FormatClasse(self,classe):
#         cl =""
#         if classe == "" or classe == " ":
#             return False
#         else:
#             cl = classe[0]+" "+"ieme"+" "+classe[len(classe) - 1]
#         return cl
#       #notes
#   def noteValide(self,note):
#         matieresNotes = note.split("#")
#         if matieresNotes[0] == '':
#             del matieresNotes[0]
#         else:
#             pass    
#         listeMat = []
#         for mat in matieresNotes:
#             matSub = re.sub('[|]',':',mat)
#             matSub = matSub.replace(']',':')
#             matSub = matSub.replace('[',':')
#             matSub = matSub.replace(',','.')
#             matSub = matSub.replace(" ","")
#             matSub = matSub.replace(';',':')
#             matSub = matSub.split(':')
#             del matSub[len(matSub) -1]
#             if matSub == "" or matSub == " " or len(matSub) <= 1:
#                 return False
#             for i in range(1,len(matSub)): 
#                 for c in matSub[i]:
#                     if c not in ["0","1","2","3","4","5","6","7","8","9","."]:
#                         return False   
#             matSub = "-".join(matSub)
#             matSub = matSub.strip()
#             matSub = matSub.split("-")
#             for i in range(len(matSub)):
#                 if matSub[i] == "" or matSub[i] == " ":
#                     matSub[i] = matSub[i].replace("","0.0")            
#             s = 0
#             nbr = 0
#             moy = 1
#             examen = 0
#             for i in range(1,len(matSub)- 1):
#                 # if(float(matSub[i]) < 0 and float(matSub[i]) > 20):
#                 #     return False
#                 # else:
#                 s += float(matSub[i])
#                 nbr += 1      
#             examen += float(matSub[len(matSub) - 1])  
#             moy += round((((s / nbr) + 2*examen) / 3),2)
#             matSub.append(moy)
#             listeMat.append(matSub)
#             matSub=[]    
#         return listeMat
  

#   def affiche_eleves(self):
#       print(f"""
#            Nom:{self.Nom} 
#            Prénom:{self.Prénom}
#            Numeros:{self.Numeros}  
#            Note:{self.Note}  
#            Classe:{self.Classe}
#            Naissance:{self.Naissance}         
#            """)

# print(Etudiant.dateValide("self",Etudiant.changerFormatDate("self","28/février/2003")))






#Le code définit une méthode appelée "affiche_eleves" 
# pour une classe non précisée. Cette méthode a pour but 
# d'afficher les informations relatives à un élève.


  
      
# data=Donnee('Project.csv')   
# mesdonnees=data.recup_valeurs()
# for unedonnee in mesdonnees:
#    ettudiant =Etudiant(mesdonnees)
#    ettudiant.affiche_eleves  
# print("recuperation des donnes")


    
    
    
    
print("\n\n")

      


 