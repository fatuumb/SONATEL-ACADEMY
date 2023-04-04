   #importer la fonction exit
from sys import exit

   #creation d'une fonction pour le menue
def menue():

    while True:
        print("\n")
        print("*****************************MENU**********************************")
        print("*******************************************************************")

        #print("__________________________________________________________________")
    
        print("1.  Taper 1 pour Le Francais\n"+"2.  Taper 2 pour L'Anglais\n"+"3.  Taper 3 pour Quitter\n")

        a=int(input("\tFaite votre choix\n"))

        print("**************************************************************")

#menue()
        if a==1:
                print('\n-------------------tableau des mois en Français------------------')
                affichage(Mois_français)
        elif a==2:
            
            print('\n---------------------tableau des mois en Anglais----------------')
            affichage(Mois_anglais)
        elif a==3:
            print("Merci d'avoir visiter notre programme!!")
            exit()


  #creation d'une fonction pour l'affichage
def affichage(M):
    print('_________________________________________________________________')

    for i in range (0,3):

            print(("|"+M[i])+"|"+(M[i+3])+"|"+(M[i+6])+"|"+(M[i+9])+"|")
            print("|_______________|_______________|_______________|_______________|")

#creation des 2 tableau de mois
Mois_français=['Janvier  \t','février   \t','mars    \t','avril\t\t','mai \t\t','juin     \t','juillet \t','aout   \t','septembre    \t','octobre\t','novembre\t','décembre\t']    
Mois_anglais=['january  \t','february   \t','march    \t','april\t\t','may \t\t','jun     \t','july   \t','august   \t','september    \t','october\t','november\t','décember\t']    

print("\n")
print("\t*********Programme mois********* \t")
print('_________________________________________________________________')

for i in range (0,3):

    print(("|"+Mois_français[i])+"|"+(Mois_français[i+3])+"|"+(Mois_français[i+6])+"|"+(Mois_français[i+9])+"|")
print("|_______________|_______________|_______________|_______________|")
menue()





