import random

# 1. Mostrar opciones
print("=== JUEGO PIEDRA, PAPEL O TIJERA ===")
print("1 = Piedra")
print("2 = Papel")
print("3 = Tijera")

# 2. Solicitar al usuario que ingrese su elección
usuario = input("Ingresa tu elección (1-3): ")

# 3. Validar que la opción sea correcta
while usuario not in ["1", "2", "3"]:
    print("Opción inválida. Intenta nuevamente.")
    usuario = input("Ingresa 1, 2 o 3: ")

# Convertir a número
usuario = int(usuario)

# 4. Generar número aleatorio entre 1 y 3
computadora = random.randint(1, 3)

# 5. Asignar nombre a cada opción
opciones = {
    1: "piedra",
    2: "papel",
    3: "tijera"
}

# 6. Mostrar elección de la computadora
print(f"La computadora eligió: {opciones[computadora]}")

# 7. Comparar elecciones
if usuario == computadora:
    resultado = "Empate"
elif (usuario == 1 and computadora == 3) or \
     (usuario == 2 and computadora == 1) or \
     (usuario == 3 and computadora == 2):
    resultado = "Ganaste"
else:
    resultado = "Perdiste"

# 8. Mostrar resultado
print(f"Resultado del juego: {resultado}")