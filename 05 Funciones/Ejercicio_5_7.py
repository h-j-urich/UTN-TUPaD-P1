"""  7. Crear una función llamada operaciones_basicas(a, b) que reciba
 dos números como parámetros y devuelva una tupla con el resulta
do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re
sultados de forma clara"""

def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    return (suma, resta, multiplicacion, division)

num1 =  int(input("ingrese un numero: "))
num2 =  int(input("ingrese otro numero: "))

resultados = operaciones_basicas(num1, num2) 

print(f"La suma de {num1} mas {num2} es = {resultados[0]}")
print(f"La resta de {num1} menos {num2} es = {resultados[1]}")
print(f"La multiplicacion de {num1} por {num2} es = {resultados[2]}")
print(f"La division de {num1} dividido {num2} es = {resultados[3]:.2f}")

