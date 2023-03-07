#Importez les fonctions et modules nécessaires.
import Fonctions as pf
# from Fonctions import*
from csv import DictReader



lignes_valides =[]
lignes_non_valides =[]

mainfichier_csv = dict()
compt = 0
tab=[]
with open('Project.csv', 'r') as fichier_csv:

    fichier_csv_reader = DictReader(fichier_csv)
    for ligne in fichier_csv_reader:
        tab.append(ligne)

#creation de 2 dictionnaire d qui recupere les  
#elements valide et erreur qui recupere 
#les elements non valides 

for i in range (0,len(tab)):
    d={}
    erreur={}
    is_valide=True
   
#num
    d["Numero"]=pf.v_numero(tab[i]['Numero'])[1]
    num=pf.v_numero(tab[i]['Numero'])[0]
    if num==False:
        d["Numero"]=tab[i]['Numero']
        erreur["Numero"]=" Le Numero est invalide"
        is_valide=False
      

#prenom
    pm=pf.v_prenom(tab[i]['Prénom'])
    d["prenom"]=tab[i]['Prénom']
    if pm==False:
        d["prenom"]=tab[i]['Prénom']
        erreur["prenom"]=" Le prénom est invalide"
        is_valide=False
        
#nom
    name=pf.v_nom(tab[i]['Nom'])
    d["Nom"]=tab[i]['Nom']
    if name==False:
        d["Nom"]=tab[i]['Nom']
        erreur["Nom"]=" Le Nom est invalide"
        is_valide=False
        


#Classe
    cl=pf.v_classe(tab[i]['Classe'])

    d["Classe"]=tab[i]['Classe']
    if cl==False:
        d["Classe"]=pf.change_classe(tab[i]['Classe'])
        erreur["Classe"]=" Le Classe est invalide"
        is_valide=False

 #notes
    nt=pf.v_prenom(tab[i]['Note'])
    d["Note"]=tab[i]['Note']
    if nt==False:
        d["Note"]=tab[i]['Note']
        erreur["Note"]=" Le Note est invalide"
        is_valide=False
    if(is_valide==False):
            lignes_non_valides.append(d)       
    else:
        lignes_valides.append (d)

#--------affichages des lignes valides----------# 
# def affichage(lignes_valides):
#     print("\t_____________LES LIGNES VALIDES_______________ ") 
#     print('-------------------------------------------------------------------')
    
#     print('Numero'+(15-len('Numero'))* " "+"| "
#           +"Nom"+(15-len('Nom'))* " "+"| "
#           +"prenom"+(15-len('prenom'))* " "+"| "
#           +"Classe"+(15-len('Classe'))* " "+"| ")
#     print('-------------------------------------------------------------------')
    
    
#     for dict in lignes_valides:
        
#         print(dict['Numero']+(15-len(dict['Numero']))* " "+"|",end=" ")
#         print(dict['Nom']+(15-len(dict['Nom']))* " "+"|",end=" ")
#         print(dict['prenom']+(15-len(dict['prenom']))* " "+"|",end=" ")
#     #   print(dict['Date de naissance']+(15-len(dict['Date de naissance']))* " "+"|",end=" ")
#         print(dict['Classe']+(15-len(dict['Classe']))* " "+"|")
#         #print(dict['Note']+(15-len(dict['Note']))* " "+"|",end=" ")
#     print('-------------------------------------------------------------------')

    
#         #print('__________________________________________________________________')
        
#    # print("\n\n")
# affichage(lignes_valides)
# #--------affichages des non  lignes valides----------#  

# print("\t_____________LES LIGNES non VALIDES_____________ ") 
# print('-------------------------------------------------------------------')

# print('Numero'+(15-len('Numero'))* " "+"| "
#       +"Nom"+(15-len('Nom'))* " "+"| "
#       +"prenom"+(15-len('prenom'))* " "+"| "
#       +"Classe"+(15-len('Classe'))* " "+"| ")
# print('-------------------------------------------------------------------')


for dict in lignes_non_valides:
    
    print(dict['Numero']+(15-len(dict['Numero']))* " "+"|",end=" ")
    print(dict['Nom']+(15-len(dict['Nom']))* " "+"|",end=" ")
    print(dict['prenom']+(15-len(dict['prenom']))* " "+"|",end=" ")
#   print(dict['Date de naissance']+(15-len(dict['Date de naissance']))* " "+"|",end=" ")
    print(dict['Classe']+(15-len(dict['Classe']))* " "+"|")
    #print(dict['Note']+(15-len(dict['Note']))* " "+"|",end=" ")




#ceci est le menu de modification
# def modif_menu():
#     print("""           |
#                         |   1. Modifier une ligne invalides
#                         |   2. Afficher les erreurs
#         MODIFICATION    |   3. Afficher les lignes invalides
#                         |   4. Revenir au menu principal
#                         |   5. Pour sortir
#                         |
#     """)
#     subchoix = int(input("Faites votre choix: "))

#     if subchoix == 1:
#         modif_id = int(input("Entrez le numero de la ligne �  modifier: ").strip())
#         print("La ligne invalide est ")
#         pf.affiche_invalide(lignes_non_valides, modif_id)
#         tovalidate = pf.return_invalide(lignes_non_valides, modif_id)
#         # print(tovalidate)
#         print("Les erreurs �  corriger: ")
#         pf.affiche_invalide(sub_errors, modif_id)
#         tovalidate = pf.modifier(tovalidate)
#         if tovalidate == False:
#             print("La modification est annulée")
#             modif_menu()
#         else:
#             # suppression de la ligne dans le dico invalide
#             del lignes_non_valides[modif_id]
#             lignes_valides.setdefault(modif_id, tovalidate)
#             print("La ligne " + str(modif_id) + "est ajoutée aux lignes valides avec succees")
#             modif_menu()
#     elif subchoix == 2:
#         pf.affiche_errors(sub_errors)
#         modif_menu()
#     elif subchoix == 3:
#         pf.affiche_info(lignes_non_valides)
#         modif_menu()
#     elif subchoix == 4:
#         menu()
#     elif subchoix == 5:
#         exit()

# def menu():
#     try:
#         print("MENU")
#         print("""
#             1. Afficher les lignes valides
#             2. Afficher les lignes invalides
#             3. Afficher une information par numero
#             4. Afficher les 5 premiers
#             5. Modifier une information invalides
#             6. Mettre les lignes valides dans la base de donnees
#             Ps: Mettez 0 ou un autre chiffre pour quitter
#         """)
#         try:
#             choix = int(input("Faites votre choix: "))
#         except Exception as e:
#             menu()



#         if choix == 1:
#             print("Affichage des lignes valides")
#             pf.affiche_infov(lignes_valides)
#             menu()
            
            
            
            
#         elif choix == 2:
#             print("Affichage des lignes invalides")
#             pf.affiche_info(lignes_non_valides)
#             # print("Voir la liste des erreurs ? oui: pour voir /non: pour aller au menu")
#             # mychoix = input().lower()
#             # if mychoix =='yes':
#                # pf.affiche_errors(erreur)
#             menu()
               
                
    
#         elif choix == 3:
#             print("Affichage d'une information par numero")
#             numero = input("Entrer le numero à afficher: ").upper().strip()
#             pf.affiche_numero(lignes_valides, numero)
#             menu()
            
            
#         # elif choix == 4:
#         #     print("Affichage des cinq premiers")
#         #     pf.affiche_5premiers(lignes_valides)
#         #     menu()
            
            
#         # elif choix == 5:
#         #     print("Modification des elements invalides")
#         #     modif_menu()
            
#         elif choix == 6:
#             (lignes_valides)
#             menu()
            
            
            
#     except KeyboardInterrupt:
#         exit()
# menu()
