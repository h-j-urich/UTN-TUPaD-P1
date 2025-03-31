""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

nombre_usuario = input("Ingrese su nombre: ")
print(f"Hola! {nombre_usuario}")
print("Presione 1: si quiere su nombre en MAYUSCULAS: ")
print("Presione 2: si quiere su nombre en minusculas: ")
print("Presione 3: si quiere su nombre con la primera letra en Mayuscula: ")

opcion_usuario = int(input("Ingrese la opcion deseada: "))

if opcion_usuario == 1:
    resultado =  nombre_usuario.upper()
elif opcion_usuario == 2:
    resultado = nombre_usuario.lower()
elif opcion_usuario == 3:
    resultado = nombre_usuario.title()
else:
    resultado = "Opcion no valida!"

print("Resultado requerido: ", resultado)