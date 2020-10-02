class Matratt:
    def __init__(self, namn, pris, typ, antal_kalorier):
        self._namn = namn
        self._pris = pris
        self._typ = typ
        self._antal_kalorier = antal_kalorier

    def GetNamn(self):
        return self._namn
    
    def GetPris(self):
        return self._pris

    def GetTyp(self):
        return self._typ
    
    def GetAntalKalorier(self):
        return self._antal_kalorier

if __name__ == "__main__":

    vege = Matratt("Vegetarisk Lasagne", 100, "Vegetariskt", 900)
    vega = Matratt("Vegansk Paj", 90, "Vegansk", 850)
    kott = Matratt("Kebab Tallrik", 110, "Kött", 1200)

    mat = [vege, vega, kott]

    for i in mat:
        print(f"{i.GetNamn()}\nPris: {i.GetPris()} Kr\n{i.GetTyp()}\nKalorier: {i.GetAntalKalorier()}\n")

