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