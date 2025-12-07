import random

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
            

        computadora = random.choice(["piedra", "papel", "tijeras"])

        print("La computadora eligió:", computadora)

        if usuario == computadora:
            print("¡Es un empate!")
        elif usuario == "piedra":
            if computadora == "tijeras":
                print("¡Ganaste, %s !" % (nombre_usuario))
            else:
                print("¡La computadora ganó!")
        elif usuario == "papel":
            if computadora == "piedra":
                print("¡Ganaste, %s !" % (nombre_usuario))
            else:
                print("¡La computadora ganó!")
        elif usuario == "tijeras":
            if computadora == "papel":
                print("¡Ganaste, %s !" % (nombre_usuario))
            else:
                print("¡La computadora ganó!")
    elif opcion == "2":
        print(f"Gracias por jugar, {nombre_usuario}! ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")