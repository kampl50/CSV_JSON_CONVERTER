import re

def tablicaZLini(tekst):
    tekst=re.split('<|>|/', tekst)
    bez_spacji = []
    for string in tekst:
        if (string != ""):
            bez_spacji.append(string)
    return bez_spacji
        
f = open("testowy.xml", "r")
element=''
separator="."
przedrostek=''
koncowy_element=[]
naglowki=[]
tablica=[]
licznik=0
nr_lini=0
for linia in f:
    if(licznik==0):
        licznik+=1
        continue
    if licznik==1:
        element=linia[1:-2]
        przedrostek=element
        licznik+=1
        continue
    var=tablicaZLini(linia)

    if(len(var)==2):
        if(var[0]==element):
            nr_lini+=1
            przedrostek=element
            continue
        if(var[0] in koncowy_element):
            dl=len(var[0])
            przedrostek=przedrostek[:-dl-1]
            koncowy_element.remove(var[0])
            continue
        koncowy_element.append(var[0])
        przedrostek+=separator+var[0]
    if(len(var)==4):
        dl=len(var[0])
        przedrostek+=separator+var[0]
        if przedrostek not in naglowki:
            naglowki.append(przedrostek)
        przedrostek=przedrostek[:-dl-1]
    
f.close()
print((nr_lini+1)/2)
print(naglowki)

