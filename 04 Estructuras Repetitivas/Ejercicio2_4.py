""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene."""

numero = int(input("Ingresa un número entero: "))
cantidad_digitos = 0

# Convertimos el número a una cadena para iterar sobre sus caracteres
for i in str(abs(numero)):  
    cantidad_digitos += 1  # Sumamos uno por cada dígito

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")
