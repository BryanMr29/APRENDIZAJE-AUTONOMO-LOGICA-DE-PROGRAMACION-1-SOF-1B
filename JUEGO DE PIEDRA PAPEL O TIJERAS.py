import random

#variables para contador de puntos
puntos_usuario = 0
puntos_computadora = 0
puntos_empate = 0

#funcion para lógica de juego y para contador de puntos se definio las variables como global para indicar que son las que ya se encuentran declaradas fuera de la función y evitar errores al sumar los puntos 
def logica_de_juego(usuario, computadora):
    global puntos_usuario, puntos_computadora, puntos_empate
    if usuario == computadora:
            print("¡Es un empate!")
            puntos_empate += 1
    elif usuario == "piedra":
        if computadora == "tijeras":
            print("¡Ganaste, %s !" % (nombre_usuario))
            puntos_usuario += 1
        else:
            print("¡La computadora ganó!")
            puntos_computadora += 1
    elif usuario == "papel":
        if computadora == "piedra":
            print("¡Ganaste, %s !" % (nombre_usuario))
            puntos_usuario += 1
        else:
            print("¡La computadora ganó!")
            puntos_computadora += 1
    elif usuario == "tijeras":
        if computadora == "papel":
            print("¡Ganaste, %s !" % (nombre_usuario))
            puntos_usuario += 1
        else:
            print("¡La computadora ganó!")
            puntos_computadora += 1  
            
#funcion para mostrar puntos
def mostrar_puntos():
    print("\nPUNTOS")
    print("%s : %d" % (nombre_usuario, puntos_usuario))
    print("Computadora : %d" % (puntos_computadora))
    print("Empates : %d" % (puntos_empate))


# Pedir el nombre del usuario
nombre_usuario = input("¿Cuál es tu nombre? ")

print("¡Bienvenido al juego Piedra Papel o Tijeras, %s" % (nombre_usuario))

while True:
    print("\nOpciones:")
    print("1. Jugar")
    print("2. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("\nOpciones de juego:")
        print("1. Piedra")
        print("2. Papel")
        print("3. Tijeras")
        opcion_juego = input("Ingrese su opción: ")

        if opcion_juego == "1":
            usuario = "piedra"
        elif opcion_juego == "2":
            usuario = "papel"
        elif opcion_juego == "3":
            usuario = "tijeras"
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
            
        #La funcion random.choice selecciona aleatoriamente uno de los elementos de la lista
        computadora = random.choice(["piedra", "papel", "tijeras"])

        print("\nLa computadora eligió:", computadora)
        logica_de_juego(usuario, computadora)
        mostrar_puntos()
    
    elif opcion == "2":
        #MOSTRAR GANADOR
        if puntos_usuario < puntos_computadora:
            print("Suerte la proxima %s vez esta batalla ha terminado en empate" % (nombre_usuario))
        elif puntos_usuario > puntos_computadora :
            print("Felicidades %s, has ganado la partida" % (nombre_usuario))
        else:
            print("Suerte la proxima vez %s, la batalla ha terminado en empate" % (nombre_usuario))
        print(f"Gracias por jugar, {nombre_usuario}! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
        