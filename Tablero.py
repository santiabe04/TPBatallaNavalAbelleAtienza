import random
class Tablero:

    miRandomAnterior : str
    miRandomActual : str
    error : int

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.celdas = [[]]
    
    def crearCeldas(self):
        for fila in range(self.alto):
            for columa in range(self.ancho):
                miCelda = Celda()
                self.celdas[fila].append(miCelda)

    def apuntar(self, fila, columna):
        self.celdas[fila][columna].hayBarco()

    def crearBarcos(self, numBarcos):
        miRandomActual = ""
        miRandomAnterior = ""
        error = 0
        for i in numBarcos:
            while True :
                miRandomFila = random.randint(0,4)
                miRandomColumna = random.randint(0,4)
                miRandomActual = str(miRandomColumna) + str(miRandomFila)
                if i == 1 or miRandomAnterior != miRandomActual :
                    miBarco = Barco()
                    self.celdas[miRandomFila][miRandomColumna].agregarBarco()
                    fila = miRandomFila
                    columna = miRandomColumna
                    miRandomAnterior = str(miRandomColumna) + str(miRandomFila)
                    break