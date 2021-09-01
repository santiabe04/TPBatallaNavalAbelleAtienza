from tablero import Tablero
class Juego:
    def __init__(self):
        self.nombreJugador = self.preguntarNombreJugador()
        self.elTablero = Tablero(5,5)
        self.intentos = 0
        self.terminado = False
        self.jugar()
    
    def preguntarNombreJugador(self):
        #Para saber el nombre del jugador y tenga uno por defecto
        elNombre = str(input("Dame el nombre: "))
        print("")
        if not elNombre:
            elNombre = "Santi"
        return elNombre
    
    def jugar(self):
        while self.elTablero.largobarcoLista() != 0: #Para hacer que se rrompa el bucle al no haber más barcos
            print ("Ingrese un valor del 0 al 4")
            while True:
                try:
                    columna = int(input("Indique la columna:"))
                    fila = int(input("Indique la fila:"))
                    break
                except ValueError: #Por si hay errores de escribir algo no número
                    print ("Fila o columna no es un valor posible ")
                    continue
            self.elTablero.apuntar(fila,columna) #Llama a la función apuntar pasándoles la fila y columna ingresadas por el usuario
            self.intentos += 1
        nombreMayusculas = self.nombreJugador.upper()
        print ("FELICIDADES", (nombreMayusculas))
        print ("GANASTE  EN ", str(self.intentos), " INTENTOS")
        quit()

if __name__ == "__main__":
    miJuego = Juego()