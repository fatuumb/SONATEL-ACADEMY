from FonctionS import ProjectFichiers
import csv
# Ouvrir le fichier CSV
Fichier_csv='Projet.csv'
test=True
n=0
with open(Fichier_csv,"r") as csv_file:
    reader = csv.reader(csv_file)
    for line  in reader:
        #print(line)
        n+=1
        if(n<5):
          continue
        for l in line:
          print(l)
          test=False
        if(test==False):
          break
        