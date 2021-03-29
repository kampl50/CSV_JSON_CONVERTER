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