from AlgorithmConfig import AlgorithmConfig
import re
## Klasa, ktora obsluguje wszystkie konwersje, gdzie zródłowym plikiem jest plik o rozszerzeniu xml. Zajmuje się, odczytniem, alogrytmem przekształcenia oraz zapisem do drugiego formatu. Klasa diedziczy po klasie AlgorithmConfig, aby mieć dostęp do globalnych zmiennych konfiguracyjnych
class AlgorithmXML(AlgorithmConfig):     
    ## Konstruktor domyslny klasy AlgorithmXML
    def __init__(self):
        pass
    
    ## Metoda, która dwuwymiarową liste, zapisuje do pliku o rozszerzeniu csv, wykorzystujac sepaator kolumn z ostatniego parametru
    ## @param tab dwuwymiarowa lista, którą chcemy zapsiać do pliku csv
    ## @param file_destination ścieżka do pliku docelowego
    ## @param sep separator, który chcemy użyć przy pliku wynikowym csv
    def table2File(self,tab,file_destination,sep):
        f = open(file_destination, "w")
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                f.write(str(tab[i][j]))
                if(j!=len(tab[0])-1):
                    f.write(sep)
            f.write('\n')

    ## Metoda, która zwraca liste, gdzie elementami listy są fragemnty tekstu, stworzone w wyniku podziału tekstu przez separatory. Zwracana listwa nie zawiera elementów, które są równe "" czy też zawierają same tabulatory
    ## @param tekst tekst, który chcemy podzielić
    ## @param separatory separatory, których chemy używać do podziału tekstu. Jeśli pominiemy ten parametr to tekst będzie podzielony wzgledem znaków < > oraz /
    ## @return lista składająca się z elementów 
    def tablicaZLini(self,tekst,separatory='<|>|/'):
        tekst=re.split(separatory, tekst)
        bez_spacji = []
        for string in tekst:
            if (string != "" and string!='\t'):
                bez_spacji.append(string)
        return bez_spacji

    ## Metoda, która zwraca dwuelementową krotke. Pierwszym elementem krotki jest lista nagłówków stworzonych z pliku xml do zapisu w pliku csv(również tych zagnieżdzonych). Drugim elementem krotki jest liczba elementów w pliku xml
    ## @param filenameXML ścieżka do pliku XML, który chcemy analizować
    ## @return dwuelementowa krotka. Pierwszy element krotki to lista nagłówków a drugi element to liczba obiektów w pliku XML 
    def wyznaczNaglowki(self,filenameXML):
        f = open(filenameXML, "r")
        element=''
        przedrostek=''
        koncowy_element=[]
        naglowki=[]
        licznik=0
        nr_lini=0
        for linia in f:
            linia = re.sub(r"[\t]*", "", linia)#usuwamy tabulatory z pliku xml
            if(licznik==0):
                licznik+=1
                continue
            if licznik==1:
                element=linia[1:-2]
                licznik+=1
                continue
            var=self.tablicaZLini(linia)
            var2=self.tablicaZLini(linia,'<|>')
            if(len(var)==2):
                if(var2[0]==("/"+element)):
                    nr_lini+=1
                if(var[0]==element):
                    continue
                if(var[0] in koncowy_element):
                    dl=len(var[0])
                    przedrostek=przedrostek[:-dl-1]
                    koncowy_element.remove(var[0])
                    continue
                koncowy_element.append(var[0])
                if(przedrostek==''):
                    przedrostek+=var[0]
                else:
                    przedrostek+=self.configSeparatorKolumn+var[0]
            if(len(var)==4):
                dl=len(var[0])
                if(przedrostek==''):
                    przedrostek+=var[0]
                else:
                    przedrostek+=self.configSeparatorKolumn+var[0]
                if przedrostek not in naglowki:
                    naglowki.append(przedrostek)
                przedrostek=przedrostek[:-dl-1]
        f.close()
        return naglowki,nr_lini

    ## Metoda, która, konwertuje zawartość pliku XML i zapisuje skonwertowaną zawartość do pliku CSV
    ## @param filenameXML ścieżka do źródłowego pliku XML, który chcemy skonwertować
    ## @param fileNameCSV ścieżka do docelowego pliku CSV, gdzie chcemy zapisać skonwertowaną zawartość pliku XML
    ## @param separator separator, który chcemy użyć w docelowym pliku CSV
    def convertXML2CSV(self,filenameXML,fileNameCSV,separator):
        naglowki,nr_lini=self.wyznaczNaglowki(filenameXML)
        print(naglowki)
        lista = [[self.configJesli_brak for i in range(len(naglowki))]for j in range(nr_lini)]
        koncowy_element=[]
        licznik=0
        nr_lini=0
        przedrostek=''
        f = open(filenameXML, "r")
        for linia in f:
            linia = re.sub(r"[\t]*", "", linia)#usuwamy tabulatory z pliku xml
            if(licznik==0):
                licznik+=1
                continue
            if licznik==1:
                element=linia[1:-2]
                #przedrostek=element
                licznik+=1
                continue
            var=self.tablicaZLini(linia)
            var2=self.tablicaZLini(linia,'<|>')
            if(len(var)==2):
                if(var2[0]==("/"+element)):
                    nr_lini+=1
                if(var[0]==element):
                    #przedrostek=element
                    continue
                if(var[0] in koncowy_element):
                    dl=len(var[0])
                    przedrostek=przedrostek[:-dl-1]
                    koncowy_element.remove(var[0])
                    continue
                koncowy_element.append(var[0])
                if(przedrostek==''):
                    przedrostek+=var[0]
                else:
                    przedrostek+=self.configSeparatorKolumn+var[0]
            if(len(var)==4):
                dl=len(var[0])
                obiket=var[2]
                if(przedrostek==''):
                    przedrostek+=var[0]
                else:
                    przedrostek+=self.configSeparatorKolumn+var[0]
                par2=naglowki.index(przedrostek)
                lista[nr_lini][par2]=var[1]
                przedrostek=przedrostek[:-dl-1]
            
        f.close()
        naglowki=[naglowki]+lista
        self.table2File(naglowki,fileNameCSV,separator)


# o= AlgorithmXML()
# o.convertXML2CSV(r"C:\Users\micha\Desktop\przykładowe pliki\przykladowy_plik_xml.xml",r"C:\Users\micha\Desktop\przykładowe pliki\przykladowy_plik_xml.csv",";")