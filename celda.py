from barco import Barco
class Celda:
    def __init__(self, posicion, barco=False):
        self.posicion = posicion # tiene la forma (x,y)
        self.barco = barco
        self.hundido = False
    
    def agregarBarco(self, elBarco):
        self.barco = elBarco
    
    def hayBarco(self):
        if self.barco != False:
            self.barco.tocar()
            print("HUNDIDO")
            barco = self.barco
            self.barco = False
            self.hundido = True
            return barco
        else:
            print ("AGUA")
            print("")
            self.hundido = False
        return self.hundido