""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0. """

numero = int(input("Ingresa un número entero: "))
suma_total = 0

while numero != 0:
    suma_total += numero  # Acumula la suma
    numero = int(input("Ingresa otro número entero (0 para finalizar): "))  
    
print(f"La suma total de los números ingresados es: {suma_total}")
