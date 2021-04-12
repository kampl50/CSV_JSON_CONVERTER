from AlgorithmCsv import AlgorithmCsv

#klasa majaca na celu przetestowanie klasy AlgorithmCsv
class AlgorithmCsvTest:
    
    def testCsv(self):
        print("\nTworzenie obiektu")
        obiekt=AlgorithmCsv()
        print("\nInicjalizacja jednowymairowej listy na podstawie pliku csv")
        listaJednowymiarowa=obiekt.readCsv(r"C:\Users\micha\Desktop\SEMESTR 1\TO\TO projket\CSV_JSON_CONVERTER\backend\deniro.csv",'|')
        print("\nInicjalizacja dwuwymiarowej listy na podstawie jednowymiarowej oraz liczby kolumn")
        listaDwuwymiarowa=obiekt.OneToTwoDim(listaJednowymiarowa)
        print("\nWyswietlnie informacji o CSV")     
        obiekt.infoCsv(listaDwuwymiarowa)
        print("\nWyswietlnie danych z pliku CSV") 
        obiekt.printCsv(listaDwuwymiarowa)

        
test=AlgorithmCsvTest()
test.testCsv()
