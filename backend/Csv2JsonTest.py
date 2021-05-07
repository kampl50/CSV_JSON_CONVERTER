from AlgorithmJson import AlgorithmJson
from AlgorithmCsv import AlgorithmCsv

#klasa majaca na celu przetestowanie klasy AlgorithmCsv
class Csv2JsonTest:
    def testCsv2Json(self,file_path,file_destination,sep):
        csv=AlgorithmCsv()
        json=AlgorithmJson()
        listaJednowymiarowa=csv.readCsv(file_path,sep)
        listaDwuwymiarowa=csv.OneToTwoDim(listaJednowymiarowa)
        json.fromCsv2Json(listaDwuwymiarowa,file_destination)

test=Csv2JsonTest()
test.testCsv2Json(r'C:\Users\micha\Desktop\backend\deniro.csv','cvc.json','|')


        

