import copy
import json
def rozgniezdzenie(ds,prefix= "",sep="_",poziom= 0):
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
                nowyKlucz = prefix + sep + k


            if not isinstance(v, dict):#jesli v nie jest słownikiem
                if poziom != 0: #jeśli poziom nie jest zerem
                    v = new_d.pop(k)# z new_d pobierz wartosc o kluczu k i ją przypisz do v
                    new_d[nowyKlucz] = v#do new_d o nowym kluczu dodaj wartosc v
                continue # nowa petla for k, v in d.items():
            else:#jesli v jest slownikiem
                v = new_d.pop(k)#przypisz do v nowy słownik z pod klucza k
                new_d.update(rozgniezdzenie(v, nowyKlucz, sep, poziom + 1))#zaaktualizuj v , jako prefix nasz klucz, sep jako sep, i o jeden wyzszy poziom
        new_ds.append(new_d)#dodaj wuniki do ostatecznej listy
    if flaga:#jesli flaga jest ustawiona
        return new_ds[0] #rekurencja , wróc do wywołania czyli do update
    return new_ds

def loading_file():
    #scieżka do pliku
    file_path = 'jeszcze_bardziej_zagniezdozny_json.json'

    #załadowanie pliku do json_data
    json_data = open(file_path)

    data = json.load(json_data)
    return data

slownik= loading_file()
print("==========================================")
lista_slownikow=rozgniezdzenie(slownik)
klucze=[]

for i in range(len(lista_slownikow)):
    klucze.extend(list(lista_slownikow[i].keys()))


unikalne_klucze = list( dict.fromkeys(klucze) )
liczba_wierszy=len(lista_slownikow)
liczba_kolumn=len(unikalne_klucze)
jesli_brak="-"
pusta_tablica = [[jesli_brak for i in range(liczba_kolumn)] for i in range(liczba_wierszy)]
tablica=[unikalne_klucze]+pusta_tablica
for i in range(liczba_wierszy):
    for j in range(liczba_kolumn):
        if(tablica[0][j] in lista_slownikow[i]):
            tablica[i+1][j]=lista_slownikow[i][tablica[0][j]]

print(tablica)#ostateczna tablica CSV
