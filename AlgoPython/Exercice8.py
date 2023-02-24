print("\n")
print("\t|-----------------------------------------------------------------------------------|\t")
print("\t|***********************Bienvenue dans la plateforme********************************|\t")
print("\t|-----------------------------------------------------------------------------------|\t")

print("\n")
suite="oui"
while suite=='oui':
    
    telephone=int(input("\tEntrer votre numero?:\n "))
    nom= input("\tvotre nom ?:\n ")
    prenom =  input("\tvotre prenom ?:\n ")
    classe= input("\t quelle est votre classe ?:\n ")

    note_dev = float (input("\t\tvotre note de devoir?:\n"))
    note_pro = float (input("\t\tvotre note projet ?:\n"))
    note_exa = float (input("\t\tvotre note d'examen?:\n"))
    

    # telephone=77842561
    # nom= "Sow"
    # prenom ="fatou"
    # note_dev = 12
    # note_pro = 12
    # note_exa =12
    # classe='Data'
    # note= 3   

    note= int (input ("\t\tNous allons calculer vos 3 notes\n"))
    
    
    print("\t|********************************Vos informations***********************************|\t")

    moyenne=((note_pro+note_exa+note_exa)/note)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|telephone :",telephone)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|Prenom :",prenom)
    print("\t|-----------------------------------------------------------------------------------|\t")                                                                              

    print("\t|classe :",classe)
    print("\t|-----------------------------------------------------------------------------------|\t")


    print("\t|Nom :",nom)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|Note devoir :",note_dev)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|Note projet :",note_pro)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|Note examen :",note_exa)
    print("\t|-----------------------------------------------------------------------------------|\t")

    print("\t|Votre moyenne est:",moyenne)
    print("\t|-----------------------------------------------------------------------------------|\t")

    suite=input("ecrire oui pour un autre utlisateur ou non pour quitter\n")


def validationnum(telephone):
    operateur=['78','77','76','75','70'] 
    # if  telephone[:2] not in operateur: 
    if (len(telephone)!=9) or  telephone[:2] not in operateur: 
        return False
    return True
#validation de operateur
def validationoperateur(telephone):
    operateur={'77':0,'78':0,'76':0,'75':0,'70':0}
    if validationnum(telephone):
        if telephone [:2]=="77": 
            operateur  +=1
        elif telephone [:2]=="78":
            operateur +=1
        elif telephone [:2]=="76": 
            operateur +=1
        elif telephone [:2]=="70": 
            operateur +=1
        elif telephone [:2]=="75": 
            operateur +=1    
    else:
        print("le numero n'est pas valide")
    return(operateur)














