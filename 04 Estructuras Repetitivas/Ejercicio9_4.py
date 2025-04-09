""" 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). """

cantidad_numeros = 10  # Se puedes cambiar este valor sin alterar el codigo
suma_total = 0  
contador = 0  

print(f"Ingrese {cantidad_numeros} numeros enteros:")

# Bucle para ingresar los números y calcular la suma
for i in range(1, cantidad_numeros + 1):
    numero = int(input(f"Numero {i}: "))
    suma_total += numero  # Acumulamos la suma
    contador += 1  # Incrementamos el contador

# Calcular la media
media = suma_total / contador

# Mostrar el resultado
print(f"\nLa media de los números ingresados es: {media:.2f}")
