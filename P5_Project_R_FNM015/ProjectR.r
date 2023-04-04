#data <- read.csv("Project.csv")
data <- read.csv("/home/fatima/R/Project.csv")
View(data)
      v_numero <- function(num){
      if  ((nchar(num) != 7) && grepl("^[A-Z0-9]*$", num)) { 
        num =NA
      }else{
        num = num
      }
      }
      
      v_chaine <- function(ch,taille){
        if  (nchar(ch) < taille)  { 
          ch =NA
        }else{
          ch = ch
        }
      }
      
      
      
      v_classe <- function(cl){
        if (substring(cl,1,1) %in% c("6","5","4","3") && substring(cl,nchar(cl),nchar(cl)) %in% c("A","B")) { 
        return( cl =cl) 
        }else{
          return(ch = NA)
        }
      }
      
      
      
      
      data$Date.de.naissance =as.Date(data$Date.de.naissance,"%y/%m/%d")
      
         
        for (i in 1:length(data$Numero)){
               data$Numero[i]= v_numero (data$Numero[i])
               
               data$Prénom[i]=v_chaine(data$Prénom[i],3 )
               data$Nom[i]=v_chaine(data$Nom[i],2 )
               
               data$Classe[i]=v_classe(data$Classe[i])
       #as.Date(data$Date.de.naissance[i],"%d/%m/%y")
    }
   
       
      
         
View(data)
  
  








































































































































































































# Création d'un vecteur de dates avec le format initial

# dates <-c (data$Date.de.naissance)
#  dates
#  
#  ma_date<-format(dli$dates,"%d/%m/%y")
# ma_date
 
#dates=as.Date(format(dli$dates,"%y/%b/%d"))
# dates=as.Date(dates,"%d/%m/%y")
#dates
#replace(dates,"-","/")
# dates



# dates <-c (data$Date.de.naissance)
# 
#  ma_date <- dates
#  nouveau_format <- format(ma_date, "%d/%m/%Y")
#  nouveau_format

   # dates = as.Date("23-decembre-1994", format = "%d %b %Y")
   # dates
#   


# Conversion en objets de type date
#dates <- as.Date(dates)

# Modification du format des dates
# dates_format <- format(dates, "%d/%m/%Y")

# Affichage des dates avec le nouveau format
# dates_format






     
