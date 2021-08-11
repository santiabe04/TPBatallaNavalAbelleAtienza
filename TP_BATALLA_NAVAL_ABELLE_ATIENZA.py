'''TP BATALLA NAVAL ABELLE Y ATIENZA'''

#BIBLIOTECAS

import random

#CLASES

class Juego:
    def __init__(self):
        self.nombreJugador = self.preguntarNombreJugador()
        self.elTablero = Tablero(5,5)
        self.numBarcos = 8
    
    def preguntarNombreJugador(self):
        elNombre = input("dame el nombre")
        return elNombre
    
    def jugar(self):
        columna = input("indique la columna")
        fila = input("indique la fila")
        return self.elTablero.apuntar(fila,columna)
        """self.elTablero.apuntar(1,1)"""

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

class Barco:
    def __init__(self):
        self.vivo = True
    
    def tocar(self):
        self.vivo = False