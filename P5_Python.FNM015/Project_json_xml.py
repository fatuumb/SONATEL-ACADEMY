import csv
import json

#je crée un fichier JSON a partir du fichier csv
fichier="Project.csv"
with open(fichier,"r") as fichier:
    csv_reader= csv.DictReader(fichier)
    json_tab=[]
    for i in csv_reader:
        if '' not in i:
            json_tab.append(i)
   
    
with open('Project.csv',"w")as f:
    json.dump(json_tab,f,indent=4)
    
#je crée un fichier XML a partir du fichier csv  

data="Project.csv"
with open (data,'r') as data:
    data_reader=csv.reader(data)
    
    lmx=''
    for i in data_reader:
        xml_format='''
        <Eleve>
                    <Numero> %s </Numero>
                    <Nom> %s </Nom>
                    <Prenom> %s </Prenom>
                    <Date_de_naissance> %s </Date_de_naissance>
                    <Classe> %s </Classe>
                    <Note> %s </Note> 
        </Eleve>
        '''%(i[1],i[2],i[3],i[4],i[5],i[6])
        lmx+=xml_format
    
        #print(xml_format)
                
with open ('fichier.xml','w+') as f:
        f.write('<Eleves>')
        f.write(lmx)
        f.write('</Eleves>')
    

# une fonction qui prend en entrée un document json et retourne un document xml
def json_vers_Xml(data):
    with open(data,"r")as f:
        R=json.load(f)
        lmx=''
        for i in R:
            xml_format='''
        <Eleve>
                    <Numero> %s </Numero>
                    <Nom> %s </Nom>
                    <Prenom> %s </Prenom>
                    <Date_de_naissance> %s </Date_de_naissance>
                    <Classe> %s </Classe>
                    <Note> %s </Note> 
        </Eleve>
            '''%(i['Numero'],i['Nom'],i['Prénom'],i['Date de naissance'],i['Classe'],i['Note'])
            lmx+=xml_format
    return(print(lmx))