from AlgorithmJson import AlgorithmJson
from AlgorithmCsv import AlgorithmCsv

#klasa majaca na celu przetestowanie klasy AlgorithmCsv
class AlgorithmJsonTest:
    def testJson(self):
        csv=AlgorithmCsv()
        json=AlgorithmJson()
        listaJednowymiarowa=csv.readCsv(r"C:\Users\micha\Desktop\SEMESTR 1\TO\TO projket\CSV_JSON_CONVERTER\backend\deniro.csv",'|')
        listaDwuwymiarowa=csv.OneToTwoDim(listaJednowymiarowa)
        json.fromCsv2Json(listaDwuwymiarowa,"plik_deniro.json")

test=AlgorithmJsonTest()
test.testJson()


        

