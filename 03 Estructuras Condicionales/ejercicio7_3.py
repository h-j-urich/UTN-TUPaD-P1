""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. """

entrada_usuario = input("Por favor, ingrese una frase o palabra: ")


if entrada_usuario[-1].lower() in 'aeiou':
    entrada_usuario += "!"  

print(entrada_usuario)
