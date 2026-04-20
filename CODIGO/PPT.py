import random

def mostrar_reglas():
    print("\n=== REGLAS DEL JUEGO ===")
    print("El juego seleccionado es Piedra, Papel o Tijera.")
    print("El usuario compite contra la computadora.")
    print("1 = Piedra | 2 = Papel | 3 = Tijera")
    print("Piedra vence a Tijera")
    print("Tijera vence a Papel")
    print("Papel vence a Piedra")
    print("Si ambos eligen igual, es empate\n")

def jugar():
    while True:
        print("\n=== JUEGO PIEDRA, PAPEL O TIJERA ===")
        print("1 = Piedra")
        print("2 = Papel")
        print("3 = Tijera")

        usuario = input("Ingresa tu elección (1-3): ")

        while usuario not in ["1", "2", "3"]:
            print("Opción inválida.")
            usuario = input("Ingresa 1, 2 o 3: ")

        usuario = int(usuario)
        computadora = random.randint(1, 3)

        opciones = {1: "piedra", 2: "papel", 3: "tijera"}

        print(f"La computadora eligió: {opciones[computadora]}")

        if usuario == computadora:
            print("Empate")
        elif (usuario == 1 and computadora == 3) or \
             (usuario == 2 and computadora == 1) or \
             (usuario == 3 and computadora == 2):
            print("Ganaste")
        else:
            print("Perdiste")

        repetir = input("¿Quieres volver a jugar? (s/n): ").lower()

        if repetir != "s":
            print("Gracias por jugar ")
            return False  

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar juego")
        print("2. Ver reglas")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            continuar = jugar()
            if continuar == False:
                break  
        elif opcion == "2":
            mostrar_reglas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida")

menu()