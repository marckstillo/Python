import random
while True:
    aleatorio=random.randrange(0,3)
    eligePc = ""
    print("1. PIEDRA")
    print("2. PAPEL")
    print("3. TIJERA")
    opcion = int(input("ELIGE UNA OPCIÓN: "))

    if opcion == 1:
        eligeUsuario = "PIEDRA"
    elif opcion == 2:
        eligeUsuario = "PAPEL"
    elif opcion == 3:
        eligeUsuario = "TIJERA"
    print("ELEGISTE: ", eligeUsuario)

    if aleatorio == 0:
        eligePc = "PIEDRA"
    elif aleatorio == 1:
        eligePc = "PAPEL"
    elif aleatorio == 2:
        eligePc = "TIJERA"
    print("LA MAQUINA ELIGIO: ", eligePc)
    print("...")

    if eligePc == "PIEDRA" and eligeUsuario == "PAPEL":
        print ("GANASTE, PAPEL ENVUELVE A PIEDRA")
    elif eligePc == "PAPEL" and eligeUsuario == "TIJERA":
        print ("GANASTE, TIJERA CORTA PAPEL")
    elif eligePc == "TIJERA" and eligeUsuario == "PIEDRA":
        print ("GANASTE, PIEDRA MACHACA TIJERA")
    if eligePc == "PAPEL" and eligeUsuario == "PIEDRA":
        print ("PERDISTE, PAPEL ENVUELVE A PIEDRA")
    elif eligePc == "TIJERA" and eligeUsuario == "PAPEL":
        print ("PERDISTE, TIJERA CORTA PAPEL")
    elif eligePc == "PIEDRA" and eligeUsuario == "TIJERA":
        print ("PERDISTE, PIEDRA MACHACA TIJERA")
    elif eligePc == eligeUsuario:
        print("EMPATE")
    