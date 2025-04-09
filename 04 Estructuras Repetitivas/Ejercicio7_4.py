""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
número entero positivo indicado por el usuario."""

# Se solicita un numero entero positivo al usuario

num = int(input("Ingrese un numero entero positivo: "))

suma = 0
# En el bucle for se suma todas las iteraciones incluido el ingresado por el usuario
for i in range(num+1): 
    suma += i

print(f"La suma de los numero del 0 al {num}, da como resultado: {suma}")