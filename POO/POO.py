from csv import DictReader

nameinfichier_csv = dict()
compt = 0
with open('Project.csv','r') as fichier_csv:

    fichier_csv_reader = DictReader(fichier_csv)
    for line in fichier_csv_reader:
      print("\n\n")
      print(line)

#creation de la classe
class Etudiant:
    # constructeur
    def __init__(self):
        #pass  # passe au suivant. elle ne fait rien cette fonction pass
        self.prenom = line[1]
        self.nom    = line[2]
        self.Notes  = line[3]
        self.Numeros= line[3]
        self.Classe  = line[5]
print("recuperation des donnes")



