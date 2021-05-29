import re

class AlgorithmXML():     
    ## Konstruktor
    def __init__(self):
        self.csvFile=None
        self.separatorNaglowkow='.'


    def table2File(self,tab,file_destination,sep):
        f = open(file_destination, "w")
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                f.write(str(tab[i][j]))
                if(j!=len(tab[0])-1):
                    f.write(sep)
            f.write('\n')

    def tablicaZLini(self,tekst,separatory='<|>|/'):
        tekst=re.split(separatory, tekst)
        bez_spacji = []
        for string in tekst:
            if (string != "" and string!='\t'):
                bez_spacji.append(string)
        return bez_spacji

    def wyznaczNaglowki(self,filenameXML):
        f = open(filenameXML, "r")
        element=''
        przedrostek=''
        koncowy_element=[]
        naglowki=[]
        tablica=[]
        licznik=0
        nr_lini=0
        for linia in f:
            linia = re.sub(r"[\t]*", "", linia)#usuwamy tabulatory z pliku xml
            if(licznik==0):
                licznik+=1
                continue
            if licznik==1:
                element=linia[1:-2]
                przedrostek=element
                licznik+=1
                continue
            var=self.tablicaZLini(linia)
            var2=self.tablicaZLini(linia,'<|>')
            if(len(var)==2):
                if(var2[0]==("/"+element)):
                    nr_lini+=1
                if(var[0]==element):
                    przedrostek=element
                    continue
                if(var[0] in koncowy_element):
                    dl=len(var[0])
                    przedrostek=przedrostek[:-dl-1]
                    koncowy_element.remove(var[0])
                    continue
                koncowy_element.append(var[0])
                przedrostek+=self.separatorNaglowkow+var[0]
            if(len(var)==4):
                dl=len(var[0])
                przedrostek+=self.separatorNaglowkow+var[0]
                if przedrostek not in naglowki:
                    naglowki.append(przedrostek)
                przedrostek=przedrostek[:-dl-1]
        f.close()
        return koncowy_element,naglowki,nr_lini


    def convertXML2CSV(self,filenameXML,fileNameCSV,separator):
        koncowy_element,naglowki,nr_lini=self.wyznaczNaglowki(filenameXML)
        jesli_brak="-"
        lista = [[jesli_brak for i in range(len(naglowki))]for j in range(nr_lini)]
        licznik=0
        nr_lini=0
        f = open("testowy2.xml", "r")
        for linia in f:
            linia = re.sub(r"[\t]*", "", linia)#usuwamy tabulatory z pliku xml
            if(licznik==0):
                licznik+=1
                continue
            if licznik==1:
                element=linia[1:-2]
                przedrostek=element
                licznik+=1
                continue
            var=self.tablicaZLini(linia)
            var2=self.tablicaZLini(linia,'<|>')
            if(len(var)==2):
                if(var2[0]==("/"+element)):
                    nr_lini+=1
                if(var[0]==element):
                    przedrostek=element
                    continue
                if(var[0] in koncowy_element):
                    dl=len(var[0])
                    przedrostek=przedrostek[:-dl-1]
                    koncowy_element.remove(var[0])
                    continue
                koncowy_element.append(var[0])
                przedrostek+=self.separatorNaglowkow+var[0]
            if(len(var)==4):
                dl=len(var[0])
                obiket=var[2]
                przedrostek+=self.separatorNaglowkow+var[0]
                par2=naglowki.index(przedrostek)
                lista[nr_lini][par2]=var[1]
                przedrostek=przedrostek[:-dl-1]
            
        f.close()
        naglowki=[naglowki]+lista
        self.table2File(naglowki,fileNameCSV,separator)

# o=AlgorithmXML()
# o.convertXML2CSV("testowy2.xml","tojestnowacsvalka.csv","|")