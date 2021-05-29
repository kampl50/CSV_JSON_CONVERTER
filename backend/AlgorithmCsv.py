import re
import os

class AlgorithmCsv():     
    ## Konstruktor
    def __init__(self):
        self.csvFile=None
        self.columnNumber=0
        self.rowNumber=0
  

    ## Funckja wczytujaca plik csv do pola klasy
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

    ## Funckja konwertuje jednowymiarowa liste na dwuwymiarowa zwgledem liczby kolumn
    ## @param tab lista jednowymiarowa 
    ## @return zwraca dwuwymiarowa lista stworzona na podstawie jednowymiarowej listy podanej jako parametr i liczba kolumn
    def OneToTwoDim(self,tab):
        #liczba kolumn
        n=self.columnNumber
        # zwracana składa dwuwymiarowa lista
        return [tab[i:i+n] for i in range(0, len(tab), n)]
    
    ## Funckja wyswietla informacje o pliku csv, takie jak liczba kolumn, wierszy oraz nagłówki
    ## @param tab lista jednowymiarowa 
    def infoCsv(self,tab):
        print("Nagłówki kolumn:")
        for column in tab[0]:
            print(column)
        print("Liczba kolumn: ",self.columnNumber)
        print("Liczba wierszy: ",self.rowNumber-1)

    ## Funckja wyswietla zawartosc odczytanego pliku csv
    ## @param tab lista jednowymiarowa 
    def printCsv(self,tab):
        for row in tab:
            for cell in row:
                print(" {:16s}" .format(cell),end="")
            print()


    def tablicaZLini(self,tekst,separator='.'):
        tekst=re.split(separator, tekst)
        bez_spacji = []
        for string in tekst:
            if (string != "" and string!='\t'):
                bez_spacji.append(string)
        return bez_spacji

    def diffOfList(self,list_1,list_2):
        for self.elementDoXML in list_1:
            if self.elementDoXML in list_2:
                list_2.remove(self.elementDoXML)
        return list_2

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

    def readCSVWithDot(self,filenameCSV,separator):
        f = open(filenameCSV, "r")
        element=''
        liczba_wierszy=-1#-1 bo pierwszy wiersz to naglowek ktorego nie liczmy
        liczba_kolumn=0
        for linia in f:
            if(liczba_wierszy==-1):
                naglowki=linia.split(separator)
                element=linia.split(separator)[0].split(".")[0]
            liczba_wierszy+=1
        liczba_kolumn=len(naglowki)
        f.close()
        return element, liczba_wierszy,liczba_kolumn,naglowki




    def convertCSV2XML(self,filenameCSV,filenameXML,separator):

        element, liczba_wierszy,liczba_kolumn,naglowki = self.readCSVWithDot(filenameCSV,separator)
        listaJednowymiarowa=self.readCsv(filenameCSV,separator)
        listaDwuwymiarowa=self.OneToTwoDim(listaJednowymiarowa)

        ile_tab=0
        fxml=open(filenameXML,"w")
        fxml.write("<root>\n")
        ile_tab+=1
        for i in range(liczba_wierszy):
            aktualny_wiersz=i+1
            fxml.write(ile_tab*"\t"+"<"+element+">\n")
            ile_tab+=1
            zapamietane_naglowki=[element]
            for j in range(liczba_kolumn):
                if(listaDwuwymiarowa[aktualny_wiersz][j]!="-"):
                    aktualny_naglowek=naglowki[j].split(".")
                    
                    k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)
                    if(k<len(zapamietane_naglowki)):
                        for l in range(len(zapamietane_naglowki)-k):
                            ile_tab-=1
                            fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                            
                            zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                    aktualny_naglowek=self.diffOfList(zapamietane_naglowki,aktualny_naglowek)
                    
            
                    
                    if(len(aktualny_naglowek)==1):
                        fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                    else:

                        k=self.doKtoregoMiejscaZgodnosc(zapamietane_naglowki,aktualny_naglowek)
                        if(k!=0):
                            for l in range(len(zapamietane_naglowki)-k):
                                ile_tab-=1
                                fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                                
                                zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        
                        
                        
                        while(len(aktualny_naglowek)>1):
                            fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">\n")
                            ile_tab+=1
                            zapamietane_naglowki.append(aktualny_naglowek[0])
                            aktualny_naglowek.remove(aktualny_naglowek[0])
                        fxml.write(ile_tab*"\t"+"<"+str(aktualny_naglowek[0].split("\n")[0])+">"+listaDwuwymiarowa[aktualny_wiersz][j]+"</"+str(aktualny_naglowek[0].split("\n")[0])+">\n")

            
            for m in range(len(zapamietane_naglowki)):
                ile_tab-=1
                fxml.write(ile_tab*"\t"+"</"+str(zapamietane_naglowki[-1].split("\n")[0])+">\n")
                zapamietane_naglowki.remove(zapamietane_naglowki[-1])
                        

        fxml.write("</root>\n")
        fxml.close()

    def dodajPrzecinki(self,filenameJSON):
        lista=[]
        fjson=open("przecinek"+filenameJSON,"r")

        lista=[]
        for linia in fjson:
            lista.append(linia.count("\t"))
        fjson.close()

        licznik=0
        with open(filenameJSON, 'w') as out_file:
            with open("przecinek"+filenameJSON, 'r') as in_file:
                for line in in_file:
                    if(licznik<len(lista)-1):
                        if(lista[licznik]==lista[licznik+1]):
                            out_file.write(line.rstrip('\n') + "," + '\n')
                        else:
                            out_file.write(line)
                    else:
                        out_file.write(line)
                    licznik+=1
        os.remove("przecinek"+filenameJSON)



    def convertCSV2JSON(self,filenameCSV,filenameJSON,separator):
        element, liczba_wierszy,liczba_kolumn,naglowki = self.readCSVWithDot(filenameCSV,separator)
        listaJednowymiarowa=self.readCsv(filenameCSV,separator)
        listaDwuwymiarowa=self.OneToTwoDim(listaJednowymiarowa)
        ile_tab=0
        fjson=open("przecinek"+filenameJSON,"w")
        fjson.write("[\n")
        ile_tab+=1
        for i in range(liczba_wierszy):
            aktualny_wiersz=i+1
            fjson.write(ile_tab*"\t"+"{\n")
            ile_tab+=1
            zapamietane_naglowki=[]
            for j in range(liczba_kolumn):
                if(listaDwuwymiarowa[aktualny_wiersz][j]!="-"):
                    aktualny_naglowek=naglowki[j].split(".")
                    
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

# o = AlgorithmCsv()
# o.convertCSV2XML("csvalkaZXmla.csv","mojnowyplikxml.xml","|")