""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

# Definir la cantidad de números a ingresar (puede cambiarse fácilmente)
cantidad_numeros = 10  

pares = 0
impares = 0
positivos = 0
negativos = 0

# Pedir al usuario que ingrese los números
print(f"Ingresa {cantidad_numeros} números enteros:")

for i in range(1, cantidad_numeros +1):
    numero = int(input(f"Numero {i}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")
