quitter=False
while quitter==False:
    print(
    "\t1 Afficher tous les étudiants \n",
    "\t2 Trier et afficher (par ordre décroissant de la moyenne) \n",
    "\t3 Rechercher selon un critère (téléphone, nom, prénom ou classe) \n",
    "\t4 Modification de notes pour un étudiant choisit par l’utilisateur en donnant le numéro de téléphone \n",
    "\t5 Sortir (permet de terminer l’application)"
)
    choix=input("Saisissez votre choix")
    #voir si le choix est un nombre
    print(choix)
    try:
        choix=int(choix)
        
        if choix==5:
            quitter=True
        elif choix==1:
            print("Afficher...")
        elif choix==2:
            print("trier par...")
        elif choix==3:
            print("Recherche...")
        elif choix==4:
            print("Modif Note...")
        else:
            print("Choix indisponible")    

    except:
        print("Choix le choix doit etre un nombre")