""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

num = int(input("Ingrese un numero entero para determinar las sifras que posee: "))

# Convertir el número a cadena, invertirlo y convertirlo nuevamente a entero
numero_invertido = int(str(num)[::-1])

print(f"El número invertido es: {numero_invertido}")
