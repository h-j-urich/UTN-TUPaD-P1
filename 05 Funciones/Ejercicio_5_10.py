"""  10.Crear una función llamada calcular_promedio(a, b, c) que reciba
 tres números como parámetros y devuelva el promedio de ellos.
 Solicitar los números al usuario y mostrar el resultado usando esta
 función."""


def calcular_promedio(a, b, c):
    return (a + b + c) / 3

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

promedio = calcular_promedio(nota1, nota2, nota3)

print(f"El promedio general es {promedio:.2f}")