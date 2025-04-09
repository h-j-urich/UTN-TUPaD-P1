""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores. """


num_inicio = int(input("Ingresa el primer número: "))
num_fin = int(input("Ingresa el segundo número: "))

# Asegurar que el primer número sea menor que el segundo, sino intercambiar valores
if num_inicio > num_fin:
    num_inicio, num_fin = num_fin, num_inicio  

suma = 0

# Iterar sobre el rango excluyendo los valores extremos
for i in range(num_inicio + 1, num_fin):
    suma += i

print(f"La suma de los números entre {num_inicio} y {num_fin}, excluyendo esos valores, es: {suma}")
