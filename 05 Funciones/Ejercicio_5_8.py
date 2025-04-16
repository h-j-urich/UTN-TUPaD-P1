"""  8. Crear una función llamada calcular_imc(peso, altura) que reciba el
 peso en kilogramos y la altura en metros, y devuelva el índice de
 masa corporal (IMC). Solicitar al usuario los datos y llamar a la función 
 para mostrar el resultado con dos decimales."""


def calcular_imc(peso, altura):
    return peso / (altura ** 2)
    
pedir_peso = float(input("Ingrese su peso: "))
pedir_altura = float(input("Ingrese su altura: "))

resultado_IMC = calcular_imc(pedir_peso, pedir_altura)

print(f"El IMC de usted es {resultado_IMC:.2f}")

