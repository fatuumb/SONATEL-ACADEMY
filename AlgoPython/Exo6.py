# grande_matrice=int(input("Veiller saisir l'ordre de la matrice superieur a 4 : \n"))
grande_matrice=6
if grande_matrice<4:
    print("la taille doit etre superieur 4 \n")
matrice=[[0 for i in range(grande_matrice)]for j in range(grande_matrice)]
for i in range(grande_matrice):
       for j in range(grande_matrice) :
            matrice[i][j]=0

tab_position=["ADDP","EDDP","SDP","ADDS","EDDS","SDS"]
tab_couleur=["blanc","Vert","bleu" ,"Jaune ","rouge","Rose"]
print("la position doit etre parmi les element de tab_position",tab_position)
# choix_couleur=input("donner votre couleur : \n")
# choix_position=input("donner votre position : \n")
choix_position="SDS"
choix_couleur= "bleu"


for k in range(len(tab_couleur)):
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[5]):
            color="\033[1;{}m1".format(str(46))

            for i in range(grande_matrice):
                # for j in range(grande_matrice):
                     matrice[i][grande_matrice-i-1]=color
                     
                    


        
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[2]):
            for i in range(grande_matrice):
                matrice[i][i]=1
        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[0]):
            for i in range(grande_matrice):
                for j in range(grande_matrice):  
                    if i<j: 

                        color="\033[1;{}m1".format(str(42))
                        matrice[i][j]=color



        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[1]):
            for i in range(grande_matrice):
                for j in range(grande_matrice):
                    if i>j:
                        color="\033[1;{}m1".format(str(43))
                        matrice[i][j]=color



        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[4]):
            for i in range(grande_matrice):
                for j in range(grande_matrice):
                    if(i+j)>grande_matrice-1:
                        color="\033[1;{}m1".format(str(47))

                        matrice[i][j]=color



        if (choix_couleur==tab_couleur[k] and choix_position==tab_position[3]):
            for i in range(grande_matrice):
                for j in range(grande_matrice):
                 if(i+j)<grande_matrice-1:
                     color="\033[1;{}m1".format(str(45))
                     matrice[j][i]=color
                     

for i in range(grande_matrice):
    for  j in range(grande_matrice):                 
        print(matrice[i][j],end=(5*" "))
    print("\n")

   