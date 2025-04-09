""" 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random  # Importamos el módulo para generar números aleatorios

numero_secreto = random.randint(0, 9)

intentos = 0

print("Intenta adivinar el número secreto entre 0 y 9.")
# Inicializamos con un valor distinto para entrar al bucle
numero_usuario = -1  

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Ingresa tu número: "))
    intentos += 1  # Aumentar el contador de intentos
    
    if numero_usuario < numero_secreto:
        print("El número secreto es mayor. Intenta nuevamente.")
    elif numero_usuario > numero_secreto:
        print("El número secreto es menor. Intenta nuevamente.")

print(f"¡Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")

