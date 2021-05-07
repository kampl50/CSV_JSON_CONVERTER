from AlgorithmJson import AlgorithmJson
class AlgorithmJson2CsvTest:
    def testJson2Csv(self,file_path,file_destination,sep):
        o=AlgorithmJson()
        slownik=o.loading_file(file_path)
        lista_slownikow=o.rozgniezdzenie(slownik)
        tablica=o.dict2Table(lista_slownikow)
        o.table2File(tablica,file_destination,sep)


test=AlgorithmJson2CsvTest()
test.testJson2Csv('jeszcze_bardziej_zagniezdozny_json.json','abc.csv','|')




