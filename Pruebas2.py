import random
miRandomAnterior = str
miRandomActual = str
for i in range (5):
    miRandomFila = random.randint(1,5)
    miRandomColumna = random.randint(1,5)
    miRandomActual = str(miRandomColumna) + str(miRandomFila)
    if i == 1 or miRandomAnterior != miRandomActual :
        print ("Se creó un barco")#miBarco = Barco()
        fila = miRandomFila
        columna = miRandomColumna
        miRandomAnterior = str(miRandomColumna) + str(miRandomFila)
    else:
        print("lol")