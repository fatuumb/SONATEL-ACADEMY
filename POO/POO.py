#creation de la classe
from csv import DictReader
from pprint import pprint
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

pprint(co)

class Etudiant:
    
  def _init_(self,information):
     
     self.information= information
     self.Nom = information["Nom"]
     self.Prénom    = information["Prénom"]
     self.Numeros  = information["Numeros"]
     self.Note= information["Note"]
     self.Classe = information['Classe']
     self.naissance = information['Date de Naissance']


#Le code définit une méthode appelée "affiche_eleves" 
# pour une classe non précisée. Cette méthode a pour but 
# d'afficher les informations relatives à un élève.


  def affiche_eleves(self):
      print(f"""
           Nom:{self.Nom} 
           Prénom:{self.Prénom}
           Numeros:{self.Numeros}  
           Note:{self.Note}  
           Classe:{self.Classe}
           Naissance:{self.Naissance}         
           """)
      
# data=Donnee('Project.csv')   
# mesdonnees=data.recup_valeurs()
# for unedonnee in mesdonnees:
#    ettudiant =Etudiant(mesdonnees)
#    ettudiant.affiche_eleves  
#print("recuperation des donnes")


    
    
    
    
#     #   print("\n\n")
#     #   print(line)
#     # constructeur
      



