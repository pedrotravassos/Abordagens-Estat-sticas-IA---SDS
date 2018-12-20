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

def criatam():
    count=1
    array=[]
    while count<len(crimes):
        array.append(0)
        count+=1
    return array

    
#pega dados do csv
tab3=pd.read_csv('./dados.csv')
pega_dados=tab3.iloc[:,28].values

#remove dados repetidos
crimes=remove_repetidos(pega_dados)

#pega dados da tabela
valores=tab3.iloc[:,[6,10,11,34,28,29]].values
#tipos de crimes
tipos=[]

#cria lista de tipos de crimes vazia
c=0
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
c=0
while c<len(tab3.index):
    #pega valor do mes
    mes=str(valores[c,5])[3:-5]

    #checa valores para busca
    if(nome==valores[c,0] and mae==valores[c,1]and nasc==str(valores[c,2]) and str(valores[c,3]).find(ano)!=-1):
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
c=0
while c<len(crimes)-1:
    s.append(s2[c]-s1[c]) 
    c+=1 
s.append(len(meses))

#se cadastro for encontrado
if(flag):
        #dados para teste
        treino=[]
        #array de crimes
        p=[]
        #array de classes
        o=[]
        saida=['cometer CVLI','nao cometer CVLI']
        #cria registros para teste
        c=0
        while c<110:
            #compara quantidade de tipos de crimes
            pos=0
            while pos<len(tipos)-1:
                #adiciona quantidade de certo crime
              treino.append(randint(-2,6))
              pos+=1
            #adiciona mes  
            treino.append(randint(1,6))
            #adiciona crimes ao indice
            p.append(treino)
            #adiciona classe ao indice
            o.append(saida[randint(0,1)])
            #reinicia
            treino=[]
            c+=1
        #inicia modelo
        modelo2 = GaussianNB()
        #treina modelo
        modelo2.fit(p,o)

        print(modelo2.classes_)
        print(modelo2.predict_proba([s]))
else:
    print("cadastro não encontrado")




