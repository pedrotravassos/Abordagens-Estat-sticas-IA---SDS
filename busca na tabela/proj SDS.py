from sklearn.naive_bayes import GaussianNB
import pandas as pd
from random import randint
import numpy as np

#função para remover os meses repeditos da lista de meses
def remove_repetidos(lista):
    #cria uma lista nova
    l = []
    for i in lista:
        #se o indice em questão não estiver na lista nova, adiciona
        if i not in l:
            l.append(i)  
    #retorna lista criada
    return l

def isnumber(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def criatam():
    count=1
    array=[]
    while count<len(crimes):
        array.append(0)
        count+=1
    return array
    
#pega dados do csv
tab=pd.read_csv('./dados.csv')
pega_dados=tab.iloc[:,28].values

#remove dados repetidos
crimes=remove_repetidos(pega_dados)

#pega dados da tabela
valores=tab.iloc[:,[6,10,11,34,28,29]].values
#tipos de crimes
tipos=[]

#cria lista de tipos de crimes vazia
c=1
while c<len(crimes):
    tipos.append(0)
    c+=1

#listas de crimes para cada semestre
s1=criatam()
s2=criatam()
#valores de busca para teste
mae=str(valores[1,1])
nome=str(valores[1,0])
nasc=str(valores[1,2])
ano='2016'

#lista de meses
meses=[]
#flag para testar se o cadastro foi encontrado
flag=False
#checa cadastro
c=1
while c<len(tab.index):
    #pega valor do mes
    mes=str(valores[c,3])[3:-5]

    #checa valores para busca
    if(nome==valores[c,0] and mae==valores[c,1] and nasc==str(valores[c,2]) and str(valores[c,3]).find(ano)!=-1):
        #encontrou registro
        flag=True
        #joga mes na lista de meses
        meses.append(mes)
        #pega valor do crime no mes
        crime=valores[c,4]
        #busca indice
        pos=0
        while(crime!=crimes[pos]):
            pos+=1
        #aidciona valor de acordo com o semestre    
        if(mes<7):
            s1[pos]+=1
        else:
            s2[pos]+=1
    c+=1


#cria array de comparação de semestres
s=[]
#organiza array de comparação dos semestres
final=[]
c=1
while c<len(tipos):
    final.append(s2[c]-s1[c])
    c+=1 
final.append(len(meses))

#se cadastro for encontrado
if(flag):
    tr=[]
    #cadastros
    cads=[]
    c=1
    o=[]
    #busca um procurado
    while c<len(valores):
        #ache uma cvli
        if (str(valores[c,5]).find("CVLI")!=-1):
            #identifica quem foi
            nome=valores[c,0]
            mae=valores[c,1]
            nasc=str(valores[c,2])
            v=str(nome)+" "+str(mae)+" "+str(nasc)
            ano=str(valores[c,3])
            s=[]
            s1=criatam()
            s2=criatam()
            #cadastra na lista
            cads.append(v)         
            ms=[]
            #pega todos os crimes
            e=1
            while e<len(valores):#
                if(nome==valores[e,0] and mae==valores[e,1] and nasc==str(valores[e,2]) and str(valores[e,3]).find(ano)!=-1):
                    #valor do mes
                    mes=str(valores[e,3])[3:-5]
                    ms.append(mes)
                    #crime cometido
                    crime=valores[e,4]
                    #busca posição do crimes
                    f=0
                    while(str(crime)!=str(crimes[f])):
                            f+=1
                    #adiciona crime de acordo com semestre

                    if(isnumber(mes) and float(mes)<7):
                        s1[f]+=1
                    else:
                        s2[f]+=1
                e+=1
            #organiza cadastro de crimes+mes
            x=1        
            while x<len(tipos):
                s.append(s2[x]-s1[x])
                x+=1 
            s.append(len(ms))
            tr.append(s)
            o.append('cometer CVLI')
            c+=1
        else:
            c+=1
    c=1
    while c<len(valores):#
        nome=str(valores[c,0])
        mae=str(valores[c,1])
        nasc=str(valores[c,2])
        ano=str(valores[c,3])
        v=nome+" "+mae+" "+nasc
        if(v in cads):
            c+=1
        else:
            s=[]
            s1=criatam()
            s2=criatam()   
            ms=[]
            e=1
            flag_cvli=True
            while e<len(valores):
                w=str(valores[e,5])
                if(nome==valores[e,0] and mae==valores[e,1] and nasc==str(valores[e,2]) and str(valores[e,3]).find(ano)!=-1 ):
                    #valor do mes
                    mes=str(valores[e,3])[3:-5]
                    ms.append(mes)
                    #crime cometido
                    crime=valores[e,4]
                    #busca posição do crimes
                    f=0
                    while(str(crime)!=str(crimes[f])):
                            f+=1
                    #adiciona crime de acordo com semestre

                    if(isnumber(mes) and float(mes)<7):   
                        s1[f]+=1
                    else:
                        s2[f]+=1
                if str(w).find("CVLI")!=-1:
                    flag_cvli=False
                    e=len(valores)
                e+=1
            x=1        
        
            if(flag_cvli):
                while x<len(tipos):
                    s.append(s2[x]-s1[x])
                    x+=1
                s.append(len(ms))
                tr.append(s)
                o.append('nao cometer CVLI')
            c+=1


    modelo = GaussianNB()
    modelo.fit(tr,o)

    print(modelo.classes_)
    print(modelo.predict_proba([final]))
       
else:
    print("cadastro não encontrado")
                

                


                          


                    
