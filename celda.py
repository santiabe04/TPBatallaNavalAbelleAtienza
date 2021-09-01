from barco import Barco
class Celda:
    def __init__(self, posicion, barco=False):
        self.posicion = posicion # tiene la forma (x,y)
        self.barco = barco
        self.hundido = False

    def agregarBarco(self, elBarco):
        '''Agregamos un barco a la celda'''
        self.barco = elBarco
    
    def hayBarco(self):
        '''Se consulta si hay un barco en la celda'''
        if self.barco != False: #Hay un barco en la celda
            self.barco.tocar()
            print("HUNDIDO")
            barco = self.barco
            self.barco = False #Se quita al barco de la celda
            self.hundido = True
            return barco
        else: #No hay un barco en la celda
            print ("AGUA")
            print("")
            self.hundido = False
        return self.hundido