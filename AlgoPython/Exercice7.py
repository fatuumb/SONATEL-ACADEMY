lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
corsp_lettre=["2","22","222","3","33","333","4","44","444","5","55","555","6","66","666","7","77","777","7777","8","88","888","9","99","999","9999","00"]

chaine=str(input("Saisir votre phrase\n"))
A=[]
B=[]
for i in range (len(chaine)):
    for j in range(len(lettre)):
        if chaine [i]==lettre[j]:
            A.append(corsp_lettre[j])
    if chaine [i] not in lettre:
        A.append(chaine[i])
B.append(A[0])
for i in range (1,len(A)):
    x=A[i]
    y=A[i-1]
    if x[0]==y[len (y)-1]:
        B.append(0)
    B.append(A[i])
for i in B:
    print (i,end='')
 