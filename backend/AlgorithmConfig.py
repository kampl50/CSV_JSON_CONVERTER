## Klasa, ktora przechowuje zmienne dotyczące konfigurowania zagniezdzeń w pliku CSV. W łatwy sposób można zmienić teskt wpisywany w pole, które jest puste lub zmienić znak rozdzielający zagniezdzone zagłowki w ostatecznym nagłówku 
class AlgorithmConfig():
    ## Konstruktor domyslny klasy AlgorithmConfig
    def __init__(self):
        pass

    configJesli_brak="-"
    configSeparatorKolumn="."
