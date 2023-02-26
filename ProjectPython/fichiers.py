#Importez les fonctions et modules nécessaires.
import Fonctions as pf

from csv import DictReader

mainfichier_csv = dict()
compt = 0
tab=[]
with open('Project.csv', 'r') as fichier_csv:

    fichier_csv_reader = DictReader(fichier_csv)
    for line in fichier_csv_reader:
        tab.append(line)
        #mainfichier_csv.setdefault(compt, line)
        #compt +=1
        # for key, value in line.items():
        #     print(key, value)
        #     print("_______________________________________________________________")
    
       # print(tab)
            


lignes_valides = dict()
lignes_non_valides = dict()

for k in mainfichier_csv.keys():
#for k in mainfichier_csv.keys():
    
    sub_errors = dict()

isvalid = True
    
for subk in mainfichier_csv[k].keys():
    if subk.lower()  == 'numero':
            numero = pf.v_numero(mainfichier_csv[k][subk])


            if numero == False:
                sub_errors.setdefault('numero', mainfichier_csv[k][subk])


    elif subk.lower() == 'nom'   :
        nom = pf.v_nom(mainfichier_csv[k][subk])


    if nom == False:
                sub_errors.setdefault('nom', mainfichier_csv[k][subk])



    elif subk.lower() == 'prenom':
            prenom = pf.v_prenom(mainfichier_csv[k][subk])


            if prenom == False:
                sub_errors.setdefault('prenom', mainfichier_csv[k][subk])


    elif subk.lower() == 'date de naissance':
            naissance = pf.v_date(str(mainfichier_csv[k][subk]))


            if naissance == False:
                sub_errors.setdefault('date de naissance', mainfichier_csv[k][subk])


    elif subk.lower() == 'classe':
            classe = pf.v_classe(mainfichier_csv[k][subk])


            if classe == False:
                sub_errors.setdefault('classe', mainfichier_csv[k][subk])


            elif subk.lower() == 'note'  :



        # ici on parcours toutes les lignes et on verifie pour chaque les elements
        #   qui sont valident ou pas et on les stocke dans des dictionnaires
        
                bool = str(mainfichier_csv[k][subk])
                notes = pf.recup_notes(str(mainfichier_csv[k][subk]))
            # mainfichier_csv[k][subk] = notes
        
        
            if notes == False:
                        sub_errors.setdefault('notes', str(mainfichier_csv[k][subk]))
        
        
            else:
                        mainfichier_csv[k][subk] = notes
                        sub_errors.setdefault(k, sub_errors)
        
        
        
            if numero and nom and prenom and naissance and classe and notes:
                mainfichier_csv[k]['Classe'] = pf.change_classe(mainfichier_csv[k]['Classe'])
                # mettre ici le formatage des naissances
                mainfichier_csv[k]['Date de naissance'] = pf.change_dformat(mainfichier_csv[k]['Date de naissance'])
                lignes_valides.setdefault(k, mainfichier_csv[k])


else:
        lignes_non_valides.setdefault(k, mainfichier_csv[k])








#ceci est le menu de modification
def modif_menu():
    print("""           |
                        |   1. Modifier une ligne invalides
                        |   2. Afficher les erreurs
        MODIFICATION    |   3. Afficher les lignes invalides
                        |   4. Revenir au menu principal
                        |   5. Pour sortir
                        |
    """)
    subchoix = int(input("Faites votre choix: "))

    if subchoix == 1:
        modif_id = int(input("Entrez le numero de la ligne �  modifier: ").strip())
        print("La ligne invalide est ")
        pf.affiche_invalide(lignes_non_valides, modif_id)
        tovalidate = pf.return_invalide(lignes_non_valides, modif_id)
        # print(tovalidate)
        print("Les erreurs �  corriger: ")
        pf.affiche_invalide(sub_errors, modif_id)
        tovalidate = pf.modifier(tovalidate)
        if tovalidate == False:
            print("La modification est annulée")
            modif_menu()
        else:
            # suppression de la ligne dans le dico invalide
            del lignes_non_valides[modif_id]
            lignes_valides.setdefault(modif_id, tovalidate)
            print("La ligne " + str(modif_id) + "est ajoutée aux lignes valides avec succees")
            modif_menu()
    elif subchoix == 2:
        pf.affiche_errors(sub_errors)
        modif_menu()
    elif subchoix == 3:
        pf.affiche_info(lignes_non_valides)
        modif_menu()
    elif subchoix == 4:
        menu()
    elif subchoix == 5:
        exit()



def menu():
    try:
        print("MENU")
        print("""
            1. Afficher les lignes valides
            2. Afficher les lignes invalides
            3. Afficher une information par numero
            4. Afficher les 5 premiers
            5. Modifier une information invalides
            6. Mettre les lignes valides dans la base de donnees
            7. Afficher les infos d'une table au choix
            Ps: Mettez 0 ou un autre chiffre pour quitter
        """)
        try:
            choix = int(input("Faites votre choix: "))
        except Exception as e:
            menu()

        if choix == 1:
            print("Affichage des lignes valides")
            pf.affiche_infov(lignes_valides)
            menu()
        elif choix == 2:
            print("Affichage des lignes invalides")
            pf.affiche_info(lignes_non_valides)
            print("Voir la liste des erreurs ? oui: pour voir /non: pour aller au menu")
            mychoix = input().lower()
            if mychoix =='yes':
                pf.affiche_errors(sub_errors)
                menu()
            else:
                menu()
        elif choix == 3:
            print("Affichage d'une information par numero")
            numero = input("Entrer le numero �  afficher: ").upper().strip()
            pf.affiche_numero(lignes_valides, numero)
            menu()
        elif choix == 4:
            print("Affichage des cinq premiers")
            pf.affiche_5premiers(lignes_valides)
            menu()
        elif choix == 5:
            print("Modification des elements invalides")
            modif_menu()
        elif choix == 6:
            (lignes_valides)
            menu()
        elif choix == 7:
            menu()
    except KeyboardInterrupt:
        exit()




menu()
