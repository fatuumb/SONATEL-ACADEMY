#creation de la classe
from csv import DictReader

class Etudiant:

  nameinfichier_csv = dict()
with open('Project.csv','r') as fichier_csv:

    fichier_csv_reader = DictReader(fichier_csv)
for line in fichier_csv_reader:
  def __init__(self):
    self.prenom = line[1]
    self.nom    = line[2]
    self.Notes  = line[3]
    self.Numeros= line[3]
    self.Classe = line[5]

 
      # print("\n\n")
      # print(line)
    # constructeur
      
    print("recuperation des donnes")



