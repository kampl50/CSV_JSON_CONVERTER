from AlgorithmConfig import AlgorithmConfig
import re
import os
## Klasa, ktora obsluguje wszystkie konwersje, gdzie zródłowym plikiem jest plik o rozszerzeniu csv. Zajmuje się, odczytniem, alogrytmem przekształcenia oraz zapisem do drugiego formatu. Klasa diedziczy po klasie AlgorithmConfig, aby mieć dostęp do globalnych zmiennych konfiguracyjnych
class AlgorithmCsv(AlgorithmConfig):     
    ## Konstruktor domyslny klasy AlgorithmCsv
    def __init__(self):
        self.csvFile=None
        self.columnNumber=0
        self.rowNumber=0
  
    ## Metoda wczytujaca plik csv do pola klasy
    ## @param path sceizka do pliku csv, ktory ma byc odczytany
    ## @param delemiter separator w pliku csv
    ## @return zwraca jednowymiarowa liste z odczytanego pliku csv
    def readCsv(self,path,delemiter):
        self.csvFile=open(path)
        tab=[]
        #analizowanie pojedynczego wiersza za pomoca for
        for row in self.csvFile:
                       
            #licznik wierszy o jeden w góre
            self.rowNumber+=1
            #usuwamy z lancucha znakowego znak konca lini
            rowTmp=row.rstrip("\n")
            #liczba elementow w rekordzie mowie o ilosci kolumn
            self.columnNumber=len(rowTmp)
            #przypisujemy do zmiennej rekord juz podzielony wiersz w postacjji listy
            rowTmp=rowTmp.split(delemiter)
            #laczenie tablic w jedna
            tab.extend(rowTmp)
            #liczba kolumn
            self.columnNumber=len(rowTmp)
        return tab

    ## Metoda konwertuje jednowymiarowa liste na dwuwymiarowa względem liczby kolumn
    ## @param tab lista jednowymiarowa 
    ## @return zwraca dwuwymiarowa lista stworzona na podstawie jednowymiarowej listy podanej jako parametr i liczba kolumn
    def OneToTwoDim(self,tab):
        #liczba kolumn
        n=self.columnNumber
        # zwracana składa dwuwymiarowa lista
        return [tab[i:i+n] for i in range(0, len(tab), n)]
    
    ## Metoda wyswietla informacje o pliku csv, takie jak liczba kolumn, wierszy oraz nagłówki
    ## @param tab lista jednowymiarowa 
    def infoCsv(self,tab):
        print("Nagłówki kolumn:")
        for column in tab[0]:
            print(column)
        print("Liczba kolumn: ",self.columnNumber)
        print("Liczba wierszy: ",self.rowNumber-1)

    ## Metoda wyswietla zawartosc odczytanego pliku csv
    ## @param tab lista jednowymiarowa 
    def printCsv(self,tab):
        for row in tab:
            for cell in row:
                print(" {:16s}" .format(cell),end="")
            print()

    ## Metoda zwraca liste elementow z listy drugiej, ktore nie znajdują się w liście pierwszej
    ## @param list_1 pierwsza lista
    ## @param list_2 druga lista
    ## @param lista zawierające elementy z drugiej listy, które nie występowały w liscie pierwszej
    def diffOfList(self,list_1,list_2):
        for self.elementDoXML in list_1:
            if self.elementDoXML in list_2:
                list_2.remove(self.elementDoXML)
        return list_2

    ## Metoda liczbe, która mówi do którego indeksu dwie listy zawierały takie same elementy
    ## @param list_1 pierwsza lista
    ## @param list_2 druga lista
    ## @param liczba, bedąca indeksem do którego obie listy były równe
    def doKtoregoMiejscaZgodnosc(self,list_1,list_2):
        i=0
        while(True):
            if(i>=len(list_1) or i>=len(list_2)):
                break
            if(list_1[i]==list_2[i]):
                i=i+1
            else:
                break
        return i

    ## Metoda która, odczytuje pliku csv i zwraca liczbe wierszy, kolumn oraz nagłówki z pierwszego wiersza pliku csv
    ## @param filenameCSV ścieżka do pliku csv
    ## @param separator który odziela kolumny w pliku csv, podanym jako parametr
    ## @return trzy elementowa krotka, gdzie pierwszy i drugi element to odpowiedni liczba wierszy oraz liczba kolumn. Trzeci element o lista zawierajaca nagłówki z pierwszego rekordu pliku csv
    def readCSVWithDot(self,filenameCSV,separator):
        f = open(filenameCSV, "r")
        #element=''
        liczba_wierszy=-1#-1 bo pierwszy wiersz to naglowek ktorego nie liczmy
        liczba_kolumn=0
        for linia in f:
            if(liczba_wierszy==-1):
                naglowki=linia.split(separator)
                #element=linia.split(separator)[0].split(self.configSeparatorKolumn)[0]
            liczba_wierszy+=1
        liczba_kolumn=len(naglowki)
        f.close()
        return  liczba_wierszy,liczba_kolumn,naglowki



    ## Metoda która, konwertuje zawartość pliku CSV i zapisuje skonwertowaną zawartość do pliku XML
    ## @param filenameCSV ścieżka do źródłowego pliku CSV, który chcemy skonwertować
    ## @param filenameXML ścieżka do docelowego pliku XML, gdzie chcemy zapisać skonwertowaną zawartość pliku CSV
    ## @param separator który odziela kolumny w pliku csv, podanym jako parametr
    def convertCSV2XML(self,filenameCSV,filenameXML,separator):
        element="obiekt"
        liczba_wierszy,liczba_kolumn,naglowki = self.readCSVWithDot(filenameCSV,separator)
        listaJednowymiarowa=self.readCsv(filenameCSV,separator)
        listaDwuwymiarowa=self.OneToTwoDim(listaJednowymiarowa)

        ile_tab=0
        fxml=open(filenameXML,"w")
        fxml.write("<root>\n")
        print("<root>\n")
        ile_tab+=1
        for i in range(liczba_wierszy):
            aktualny_wiersz=i+1
            fxml.write(ile_tab*"\t"+"<"+element+">\n")
            print(ile_tab*"\t"+"<"+element+">\n")
            ile_tab+=1
            zapamietane_naglowki=[]
            for j in range(liczba_kolumn):
                if(listaDwuwymiarowa[aktualny_wiersz][j]!=self.configJesli_brak):
                    aktualny_naglowek=naglowki[j].split(self.configSeparatorKolumn)
                    
                    k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)
                    if(k<len(zapamietane_naglowki)):
                        for l in range(len(zapamietane_naglowki)-k):
                            ile_tab-=1
                            print(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                            fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                            
                            zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                    aktualny_naglowek=self.diffOfList(zapamietane_naglowki,aktualny_naglowek)
                    
            
                    
                    if(len(aktualny_naglowek)==1):
                        fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                        print(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                    else:

                        k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)
                        if(k!=0):
                            for l in range(len(zapamietane_naglowki)-k):
                                ile_tab-=1
                                fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                                print(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                                
                                zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                        
                        while(len(aktualny_naglowek)>1):
                            print(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                            fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                            ile_tab+=1
                            zapamietane_naglowki.append(aktualny_naglowek[0])
                            aktualny_naglowek.remove(aktualny_naglowek[0])
                        print(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                        fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")

            
            for m in range(len(zapamietane_naglowki)):
                ile_tab-=1
                print(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                
            ile_tab-=1             
            print(ile_tab*"\t"+"</"+element+">\n")
            fxml.write(ile_tab*"\t"+"</"+element+">\n")
        ile_tab-=1
        fxml.write("</root>\n")
        print("</root>\n")
        fxml.close()

    ## Metoda która dodaje przecinki w odpowiednim miejscu w pliku JOSN tak aby zachowac odpowiedni format
    ## @param filenameJON ścieżka do źródłowego pliku JSON, w którym chcielibyśmy dodać przecinki
    def dodajPrzecinki(self,filenameJSON):
        lista=[]

        splicedFileName = filenameJSON.split(".")[0]
        fjson=open(splicedFileName+"tymczasowy.json","r")
        lista=[]
        for linia in fjson:
            lista.append(linia.count("\t"))
        fjson.close()

        licznik=0
        with open(filenameJSON, 'w') as out_file:
            #with open("przecinek"+filenameJSON, 'r') as in_file:
            with open(splicedFileName+"tymczasowy.json") as in_file:
                for line in in_file:
                    if(licznik<len(lista)-1):
                        if(lista[licznik]==lista[licznik+1]):
                            out_file.write(line.rstrip('\n') + "," + '\n')
                        else:
                            out_file.write(line)
                    else:
                        out_file.write(line)
                    licznik+=1
        #os.remove("przecinek"+filenameJSON)
        os.remove(splicedFileName+"tymczasowy.json")


    ## Metoda która, konwertuje zawartość pliku CSV i zapisuje skonwertowaną zawartość do pliku JSON
    ## @param filenameCSV ścieżka do źródłowego pliku CSV, który chcemy skonwertować
    ## @param filenameJSON ścieżka do docelowego pliku JSON, gdzie chcemy zapisać skonwertowaną zawartość pliku CSV
    ## @param separator który odziela kolumny w pliku csv, podanym jako parametr
    def convertCSV2JSON(self,filenameCSV,filenameJSON,separator):
        #element, liczba_wierszy,liczba_kolumn,naglowki = self.readCSVWithDot(filenameCSV,separator)
        liczba_wierszy,liczba_kolumn,naglowki = self.readCSVWithDot(filenameCSV,separator)
        listaJednowymiarowa=self.readCsv(filenameCSV,separator)
        listaDwuwymiarowa=self.OneToTwoDim(listaJednowymiarowa)
        ile_tab=0
        splicedFileName = filenameJSON.split(".")[0]

        fjson=open(splicedFileName+"tymczasowy.json","w")
        #fjson=open("przecinek"+filenameJSON,"w")
        fjson.write("[\n")
        ile_tab+=1
        for i in range(liczba_wierszy):
            aktualny_wiersz=i+1
            fjson.write(ile_tab*"\t"+"{\n")
            ile_tab+=1
            zapamietane_naglowki=[]
            for j in range(liczba_kolumn):
                if(listaDwuwymiarowa[aktualny_wiersz][j]!=self.configJesli_brak):
                    aktualny_naglowek=naglowki[j].split(self.configSeparatorKolumn)
                    
                    k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)#zamykanie zagniezdzen
                    if(k<len(zapamietane_naglowki)):
                        for l in range(len(zapamietane_naglowki)-k):
                            
                            ile_tab-=1
                            
                            fjson.write(ile_tab*"\t"+"}\n")
                            zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                    aktualny_naglowek=self.diffOfList(zapamietane_naglowki,aktualny_naglowek)
                    
            
                    
                    if(len(aktualny_naglowek)==1):
                        fjson.write(ile_tab*"\t"+"\""+str(aktualny_naglowek[0].split("\n")[0])+"\":\""+listaDwuwymiarowa[aktualny_wiersz][j]+"\"\n")
                    else:

                        k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)
                        if(k!=0):
                            for l in range(len(zapamietane_naglowki)-k):
                                ile_tab-=1
                                fjson.write(ile_tab*"\t"+"}\n")
                                zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                        
                        while(len(aktualny_naglowek)>1):#otwieranie zagniezdzen
                            fjson.write(ile_tab*"\t"+"\""+str(aktualny_naglowek[0].split("\n")[0])+"\":{\n")
                            ile_tab+=1
                            
                            zapamietane_naglowki.append(aktualny_naglowek[0])
                            aktualny_naglowek.remove(aktualny_naglowek[0])
                        fjson.write(ile_tab*"\t"+"\""+str(aktualny_naglowek[0].split("\n")[0])+"\":\""+listaDwuwymiarowa[aktualny_wiersz][j]+"\"\n")

            for m in range(len(zapamietane_naglowki)):
                
                ile_tab-=1
                fjson.write(ile_tab*"\t"+"}\n")
                zapamietane_naglowki.remove(zapamietane_naglowki[-1])

            ile_tab-=1
            fjson.write(ile_tab*"\t"+"}\n")
        fjson.write("]\n")
        fjson.close()
        self.dodajPrzecinki(filenameJSON)

# o=AlgorithmCsv()
# o.convertCSV2JSON(r"C:\Users\micha\Desktop\przykładowe pliki\przykladowy_plik_xml.csv",r"C:\Users\micha\Desktop\przykładowe pliki\przykladowy_plik_xml.json",";")
