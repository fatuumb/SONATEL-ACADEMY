print("*********************listes de numeros*********************************")
print("**************************************************************************************")
chaine=input("Numéros?\n")
#chaine="778425601 708425601 768425601"
valid_num=[]
invalid_num=[]
numero=""
chainedesortie = []


#fonction qui met les element du chaine dans un tableau
def chainetotableau(chaine):
    tab=[]
    ch_num=""
    if chaine[-1]!=" ":
        chaine+=" "
    for i in chaine:
        ch_num+=i
        if i==" ":
            tab.append(ch_num)
            ch_num=""
            continue
    return tab
print (chainetotableau(chaine))


    # fonction pour la validité des numeros
def validationnum(numero):
    operateur=['78','77','76','75','70'] 
    if  numero[:2] not in operateur: 
    #if (len(numero)!=9) or  numero[:2] not in operateur: 

        return False
    return True


    # fonction pour la validité des operateurs
def validationoperateur(numero):
    operateur={'orange':0,'kirene':0,'tigo':0,'promobile':0,'expresso':0}
    if validationnum(numero):
        if numero [:2]=="77": 
            operateur ['orange']+=1
        elif numero [:2]=="78":
            operateur ['kirene']+=1
        elif numero [:2]=="76": 
            operateur ['tigo']+=1
        elif numero [:2]=="70": 
            operateur ['expresso']+=1
        elif numero [:2]=="75": 
            operateur ['promobile']+=1    
    else:
        print("les numeros ne sont pas valide")
    return(operateur)
# op=validationoperateur(chaine)
# print(op)

nums = chainetotableau(chaine)

for k in nums:
    op=validationoperateur(k)
    print(op)
    #fonction pour  le decoupage des numeros 
def decoupernum(chaine):
    variabletampon = ''
    charvalides=['1','2','3','4','5','6','7','8','9','0']
    for caractere in chaine:
       if caractere not in charvalides:
           chainedesortie.append(variabletampon)
           variabletampon = ''
       else:
           variabletampon += caractere
    if variabletampon:
       chainedesortie.append(variabletampon)
    return(chainedesortie)
    #parcourir le tableau
tab=decoupernum(chaine)
print(tab)
for i in range(0,len (tab)):
    if tab [i]!="":
        bal=validationnum(tab [i])
        if bal:
            valid_num.append (tab [i])
        else:
                invalid_num.append(tab [i])
print(valid_num,invalid_num) 


    #fonction pour enlever les caracteres speciaux
def enleverlescaracteresspeciaux(numero):
    char=""
    for c in numero:
        if  c  in  ["1","2","3","4","5","6","7","8","9","0"] or c==[" "]:
          char+=c
        else:
            continue
    return char
# el =enleverlescaracteresspeciaux(numero)
# print(el)
print("*****************************************************************************************")




