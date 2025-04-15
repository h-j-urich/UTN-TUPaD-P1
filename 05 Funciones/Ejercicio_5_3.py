"""  3. Crear una función llamada informacion_personal(nombre, apellido,
 edad, residencia) que reciba cuatro parámetros e imprima: “Soy
 [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe
dir los datos al usuario y llamar a esta función con los valores in
gresados. """

def informacion_persona(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ")

# programa principal

nombre_pedido = input("Ingrese su nombre: ")
apellido_pedido = input("Ingrese su apellido: ")
edad_pedido = input("Ingrese su edad: ")
residencia_pedido = input("Ingrese su pais de residencia: ")


informacion_persona(nombre_pedido, apellido_pedido, edad_pedido, residencia_pedido)
