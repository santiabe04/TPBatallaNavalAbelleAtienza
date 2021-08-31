from tablero import Tablero
class Juego:
    def __init__(self):
        self.nombreJugador = self.preguntarNombreJugador()
        self.elTablero = Tablero(5,5)
        self.intentos = 0
        self.terminado = False
        self.jugar()
    
    def preguntarNombreJugador(self):
        elNombre = str(input("Dame el nombre: "))
        print("")
        if not elNombre:
            elNombre = "Santi"
        return elNombre
    
    def jugar(self):
        while self.elTablero.largobarcoLista() != 0:
            print ("Ingrese un valor del 0 al 4")
            columna = int(input("Indique la columna:"))
            fila = int(input("Indique la fila:"))
            self.elTablero.apuntar(fila,columna)
            self.intentos += 1
            # Para terminar game loop self.terminado = True
        print ("GANASTE EN ", str(self.intentos), " INTENTOS")
        print ("WARZONE VICTORY")
        quit()

if __name__ == "__main__":
    miJuego = Juego()