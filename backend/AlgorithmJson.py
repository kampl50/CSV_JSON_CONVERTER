class AlgorithmJson():     
    ## Konstruktor
    def __init__(self):
        pass

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