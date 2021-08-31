import random
from barco import Barco
from celda import Celda
class Tablero:

    def __init__(self, ancho, alto):
        self.finalizado = ""
        self.ancho = ancho
        self.alto = alto
        self.miRandomActual = str
        self.miRandomAnterior = str
        self.celdafilacolumna = list()
        self.celdas = []
        self.crearCeldas()
        self.barcoLista = []
        self.barcoListaRevolution = []
        self.barcos = 0
        self.crearBarcos()
    
    def crearCeldas(self):
        for fila in range(self.alto):
            self.celdas.append([])
            for columna in range(self.ancho):
                miCelda = Celda((fila,columna),False)
                self.celdas[fila].append(miCelda)
                #print (self.celdas)
                #self.celdafilacolumna.clear()

    def apuntar(self, fila, columna):
        while True:
            try:
                barco = self.celdas[fila][columna].hayBarco()
                if barco != False:    
                    self.barcoLista.remove(barco)
                break
            except IndexError:
                print ("Fila o columna fuera de rango")
                columna = int(input("Indique la columna:"))
                fila = int(input("Indique la fila:"))
            

    def crearBarcos(self):
        miRandomActual = ""
        miRandomAnterior = ""
        for i in range (0, 5):
            while True :
                miRandomFila = random.randint(0,4)
                miRandomColumna = random.randint(0,4)
                miRandomActual = str(miRandomColumna) + str(miRandomFila)
                if i == 0 or miRandomAnterior != miRandomActual :
                    miBarco = Barco()
                    self.celdas[miRandomFila][miRandomColumna].agregarBarco(miBarco)
                    self.barcoLista.append(miBarco)
                    print(self.barcoLista)
                    miCelda = Celda((miRandomFila,miRandomColumna), barco=True)
                    miRandomAnterior = str(miRandomColumna) + str(miRandomFila)
                    break

    def largobarcoLista(self):
        return len(self.barcoLista)