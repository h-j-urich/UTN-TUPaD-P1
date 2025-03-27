""" Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. """

print("Hola mundo!")    

""" Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para 
realizar la impresión por pantalla. """

nombre = input("Ingrese su nombre: ")
print (f"Hola {nombre}")

"""Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar 
la impresión por pantalla. """

print("Seguidamente se le solicitaran datos personales")
nombre = input("Ingrese su nombre: ")
apellido =  input("Ingese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese pais de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} anios y vivo en {residencia}")

""" Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y 
su perímetro.  """

radio = float(input("Ingrese el radio de un circulo: "))
pi = 3.1416

area = pi * radio **2
perimetro = 2 * pi * radio

print (f"El area del circulo es: {area}")
print(f"El perimetro del circulo es: {perimetro}")

""" Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a 
cuántas horas equivale."""

segundos = int(input("Introduce una determinada cantidad de segundos: "))
horas = segundos / 3600

print(f"{segundos} segundos equivale a {horas:.2f} horas")

""" Crear un programa que pida al usuario un número e imprima por pantalla la tabla de 
multiplicar de dicho número """

numero = int(input("Ingrese un numero para imprimir la tabla de multiplicar: "))

print (f"{numero} X 1 = {numero * 1}")
print (f"{numero} X 2 = {numero * 2}")
print (f"{numero} X 3 = {numero * 3}")
print (f"{numero} X 4 = {numero * 4}")
print (f"{numero} X 5 = {numero * 5}")
print (f"{numero} X 6 = {numero * 6}")
print (f"{numero} X 7 = {numero * 7}")
print (f"{numero} X 8 = {numero * 8}")
print (f"{numero} X 9 = {numero * 9}")
print (f"{numero} X 10 = {numero * 10}")


"""  Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. """

num_1 = int(input("Ingrese un numero entero distinto de 0: "))
num_2 = int(input("Ingrese un numero entero distinto de 0: "))

suma = num_1 + num_2
resta = num_1 - num_2
division = num_1 / num_2
multiplicacion = num_1 * num_2

print(f"El resultado de la suma es: {suma}, de la resta: {resta}, de la division: {division} y de la multiplicacion: {multiplicacion}  ")

"""  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
de masa corporal."""

peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

imc = peso / altura **2

print(f"Su Indice de Masa Corporal es: {imc:.2f}")

"""  Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por 
pantalla su equivalente en grados Fahrenheit. """

temperatura = float(input("Ingrese la temperatura en formato Celsius: "))

temp_convertida =  (temperatura * 1.8) + 32

print(f"La temperatura {temperatura} grados Celsius convertida en grados Fahranheit es: {temp_convertida}")

"""  Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de 
dichos números."""

print("Seguidamente se le solicitara 3 numeros para ver su promedio: ")

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

promedio = (num_1 + num_2 + num_3) / 3

print(f"El promedio de los numeros ingresados es: {promedio}")
