                         #______note de R_____

#--------------------------------------------------------------------------------#
                          #COMMENT CREER UN OBJECT
#--------------------------------------------------------------------------------#

  #<- opperateur d'assignation' 
  #ex
  a <- 2
  #on peu aussi faire 
  b = 4
  #on obtient le meme resultat 
  resultat =a+b
  nom='Sow'
  prenom='fatou'
  age='24 ans'
  taille='1.83'
  
  
  
  
  
#--------------------------------------------------------------------------------#
                        #COMMENT CREER UN VECTEUR
#--------------------------------------------------------------------------------#
  
  tailles <- c(145,165,134,23) 
  taille_m <- tailles /100
  
  # :  permet de creer un nombre qui est compris entre 2 valeurs 
  x = 1:20
  # [] permet d'extraire un element parmis d'autres
data[Numero]
  #  $  permet d'extraire un element parmis d'autres
data$Numero
  
  
  

#--------------------------------------------------------------------------------#
                             # LES FONCTIONS & ARGUMENTS
#--------------------------------------------------------------------------------#

#Quelques fonctions
  
  tailles<-c(145,165,134,23)# permet de combiner l'ensemble des argument qui se trouve dans un vecteur
  length(tailles) # pour connaitre le nombres d'elements du vecteur taille
  min (tailles)   # retourne la valeur minimum d'un vecteur de nombres
  max(tailles)    # retourne la valeur maximum d'un vecteur de nombres
  sum(tailles)    # retourne la somme de tous les elements vecteur
  range(tailles)  # retourne respectivement les valeurs min et max
  class(tailles)  # permet de verifier la classe des objects
  ls()            # pour connaitre tous les objcts qu'on a creer
  getwd()         # pour avoir le repertoire de travail
  summary()       # affiche les infos des données
  nchar()         # retourne la taille de chaque element de liste
  toupper()       #Convertis la chaine en majuscule
#Quelques Arguments
  
  tailles <- c(145,165,NA,23) #une valeur manquante NA 
  na.rm =TRUE      # enleve tout les valeurs manquante
  na.rm =FALSE     # par defaut na.rm est egale a false

#--------------------------------------------------------------------------------#
                    # IMPORTATIONS DE DONNEES
#--------------------------------------------------------------------------------#
#les fonctions
head ()    # elle permet d'afficher les 6 1er ligne
tail()    # elle permet d'afficher les 6 dernier ligne
View()     # d'afficher donnees sous forme de tableau


#--------------------------------------------------------------------------------#
                          # LES DATAFRAMES
#--------------------------------------------------------------------------------#

#fonctions
row()       # il retourne le nombre de ligne du tab
ncol()      # il retourne le nombre de collone du tab
dim()       # renvoie la dimention du tab
names()     # renvoie le noms de tous nos variables
str()       # listes les differents variable ,indique leurs type et affiche
grepl()     # permet de convertir les elements en selons les regexec
substring() # permet de parcourir les elemements d'une chaine un a un 

