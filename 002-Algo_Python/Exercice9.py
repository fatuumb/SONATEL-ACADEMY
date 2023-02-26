def Decoupage(ch,sep):
    if ch[-1]==sep:
        pass
    else:
        ch+=sep
    ligne=""
    std = []
    for i in ch:
        if i != sep:
            ligne+=i
        else:
            std.append(ligne)
            ligne=""
            continue
    return std


def Taille(list):
    k = 0
    for i in list:
        k+=1
    return k

def ajout(list,el):
    el = [el]
    list+=el
    return list

#fonction pour le tri
def Tri(e,sens):
    if sens=="asc":
        for i in range(0,Taille(e)):
            for j in range(i+1,Taille(e)):
                if e[i]["moy"] > e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
 
        return e

    else:
        for i in range(0,Taille(e)):
            for j in range(i+1,Taille(e)):
                if e[i]["moy"] < e[i+1]["moy"]:
                    e[i],e[j]=e[j],e[i]
        return e


#Fonction pour la Suppression  des èspaces entre les chiffres
def Supespace(ch):
    num=""
    for k in ch:
        if k != " ":
            num+=k
    return num

def VerificationOperateur(ch):
    num = Supespace(ch)
    for c in num:
        trouve=True
        if c <'0' or c > '9':
            trouve = False
            return trouve
        else:
            trouve=True
    return trouve


#Fonction pour Vérifier la longueur du numéro
def VerificationOperateur(ch):
    num = Supespace(ch)
    if VerificationOperateur(num):
        if Taille(num) == 9:
            if num[0]+num[1] in ['77','78','76','70','75']:
                return num
            else:
                return False
        else:
            return False
    else:
        return False


def Client(list,number):
    t = False
    for k in list:
        if k["telephone"]==number:
            t = True
            break
    return t

def Operateur(name,o):
    tmp = len(o) * "\t| {:5}"
    print("\t\t",len(o[0])*len(o)*(2)*'-'+'------')
    print(name,tmp.format(*o))

def TableOperateur():
    return Decoupage(input("Entrer une liste d'opérateurs séparés par (/): "),"/" )

def AjoutClient():
    nom = input("Entrer le nom du client: ")
    prenom = input("Entrer le prénom du client: ")
    numero = input("Entrer le numéro de téléphone du client: ")
    if not VerificationOperateur(numero):
        AjoutClient()
    else:
        return {"nom":nom,"prenom":prenom,"telephone":numero}




def SaisieDeClient(clients):
    client = AjoutClient()
    if client:
        if not Client(clients,client):
            clients = ajout(clients,client)
            operateur = verifop(client["telephone"])
            return [clients,client["telephone"],operateur]
        else:
            print("Ce client existe déja")



def verifop(num):
    code = num[0]+num[1]
    if code in ["77","78"]:
        return "ORANGE"
    elif code == "76":
        return "FREE"
    elif code == "75":
        return "PROMOBILE"
    elif code == "70":
        return "EXPRESSO"
    else:
        return False
clients =[]

operateur ={}

TabOp = TableOperateur()

# AJOUT D'UN client
info = SaisieDeClient(clients)
clients = info[0]
ajout(operateur[info[2]],info[1])
ajout(TabOp,info[2])
for k in TabOp:
    if k in ["EXPRESSO","PROMOBILE","ORANGE"]:
        Operateur("\t\t {}:".format(k),operateur[k])
    else:
        Operateur("\t\t {}:\t".format(k),operateur[k])


  

  

 
 








