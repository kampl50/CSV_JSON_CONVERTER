from AlgorithmConfig import AlgorithmConfig
import copy
import json

class AlgorithmJson(AlgorithmConfig):     
    ## Konstruktor
    def __init__(self):
        pass

        #do usuniecia, jest to zwykla zamiana csv na json
    def fromCsv2Json(self,listaDwuwymiarowa,fileName):
        rowNumber=len(listaDwuwymiarowa)
        columnNumber=len(listaDwuwymiarowa[0])
        print("Liczba kolumn ",columnNumber)
        print("Liczba wierszy ",rowNumber)
        names=listaDwuwymiarowa[0]
        f = open(fileName, "w")
        f.write("[\n")
        for i in range (1,rowNumber):
            f.write("\t{\n")
            for j in range(columnNumber):
                f.write("\t\t\""+names[j]+"\":\""+listaDwuwymiarowa[i][j]+"\"")
                if(j<columnNumber-1):
                    f.write(",\n")
                else:
                    f.write("\n")
            f.write("\t}")
            if(i<rowNumber-1):
                f.write(",\n")
            else:
                f.write("\n")
        f.write("]\n")
        f.close()

    def rozgniezdzenie(self,ds,prefix= "",poziom= 0):
        flaga = False#flaga czy jestesmy w rekurencji
        if isinstance(ds, dict):#jesli ds jest słownikiem
            ds = [ds]#zamien slownik na liste
            flaga = True
        new_ds = []
        for d in ds:
            new_d = copy.deepcopy(d)
            for k, v in d.items():
                ## each key gets renamed with prefix
                #if not isinstance(k, str):
                # k = str(k)
                if poziom == 0:#jesli poziom to zero
                    nowyKlucz = k#to do nowego klucza przypisz aktualne k
                else:
                    nowyKlucz = prefix + self.configSeparatorKolumn + k
                if not isinstance(v, dict):#jesli v nie jest słownikiem
                    if poziom != 0: #jeśli poziom nie jest zerem
                        v = new_d.pop(k)# z new_d pobierz wartosc o kluczu k i ją przypisz do v
                        new_d[nowyKlucz] = v#do new_d o nowym kluczu dodaj wartosc v
                    continue # nowa petla for k, v in d.items():
                else:#jesli v jest slownikiem
                    v = new_d.pop(k)#przypisz do v nowy słownik z pod klucza k
                    new_d.update(self.rozgniezdzenie(v, nowyKlucz, poziom + 1))#zaaktualizuj v , jako prefix nasz klucz, i o jeden wyzszy poziom
            new_ds.append(new_d)#dodaj wuniki do ostatecznej listy
        if flaga:#jesli flaga jest ustawiona
            return new_ds[0] #rekurencja , wróc do wywołania czyli do update
        return new_ds

    def loading_file(self,file_path):
        #załadowanie pliku do json_data
        json_data = open(file_path)
        data = json.load(json_data)
        return data

    def dict2Table(self,lista_slownikow):
        klucze=[]
        for i in range(len(lista_slownikow)):
            klucze.extend(list(lista_slownikow[i].keys()))
        unikalne_klucze = list( dict.fromkeys(klucze) )
        liczba_wierszy=len(lista_slownikow)
        liczba_kolumn=len(unikalne_klucze)
        pusta_tablica = [[self.configJesli_brak for i in range(liczba_kolumn)] for i in range(liczba_wierszy)]
        tablica=[unikalne_klucze]+pusta_tablica
        for i in range(liczba_wierszy):
            for j in range(liczba_kolumn):
                if(tablica[0][j] in lista_slownikow[i]):
                    tablica[i+1][j]=lista_slownikow[i][tablica[0][j]]
        return tablica

    def table2File(sefl,tab,file_destination,sep):
        f = open(file_destination, "w")
        for i in range(len(tab)):
            for j in range(len(tab[0])):
                f.write(str(tab[i][j]))
                if(j!=len(tab[0])-1):
                    f.write(sep)
            f.write('\n')

    def convertJSON2CSV(self,filenameJSON,fileNameCSV,separator):
        slownik=self.loading_file(filenameJSON)
        lista_slownikow=self.rozgniezdzenie(slownik)
        tablica=self.dict2Table(lista_slownikow)
        self.table2File(tablica,fileNameCSV,separator)
    
o =AlgorithmJson()
o.convertJSON2CSV("przykladowy_plik_json.json","przykladowy_plik_csv_J.csv","|")