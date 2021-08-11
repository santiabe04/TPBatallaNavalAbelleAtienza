class Celda:
    def __init__(self, posicion):
        self.posicion = posicion
        self.barco = None
    
    def agregarBarco(self, elBarco):
        self.barco = elBarco
    
    def hayBarco(self):
        if self.barco != None:
            self.Barco.tocar()
            return True
        return False