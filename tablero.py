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
        self.barcos = 0
        self.crearBarcos()
    
    def crearCeldas(self):
        #Creamos las celdas del tablero
        for fila in range(self.alto):
            self.celdas.append([])
            for columna in range(self.ancho):
                miCelda = Celda((fila,columna),False)
                self.celdas[fila].append(miCelda)

    def apuntar(self, fila, columna):
        while True:
            try:
                barco = self.celdas[fila][columna].hayBarco()
                if barco != False:    
                    self.barcoLista.remove(barco) #Sacamos un barco de la lista
                break
            except (IndexError, ValueError):
                print ("Fila o columna fuera de rango o sin valor")
                columna = int(input("Indique la columna:"))
                fila = int(input("Indique la fila:"))
            

    def crearBarcos(self):
        miRandomActual = ""
        miRandomAnterior = ""
        for i in range (0, 5): #Cantidad de barcos
            while True :
                #Guardamos la celda para que no se repita
                miRandomFila = random.randint(0,4)
                miRandomColumna = random.randint(0,4)
                miRandomActual = str(miRandomColumna) + str(miRandomFila)
                if i == 0 or miRandomAnterior != miRandomActual :
                    miBarco = Barco()
                    self.celdas[miRandomFila][miRandomColumna].agregarBarco(miBarco)
                    self.barcoLista.append(miBarco)
                    
                    miRandomAnterior = str(miRandomColumna) + str(miRandomFila)
                    break

    def largobarcoLista(self):
        return len(self.barcoLista)