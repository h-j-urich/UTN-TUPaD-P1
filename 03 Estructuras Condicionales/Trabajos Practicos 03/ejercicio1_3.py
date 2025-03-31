"""1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, 
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. """

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")
