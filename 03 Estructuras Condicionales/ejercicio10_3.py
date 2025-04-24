""" 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año 
Periodo del año: 
Desde el 21 de diciembre hasta el 20 de 
marzo (incluidos) 
Desde el 21 de marzo hasta el 20 de junio 
(incluidos) 
Desde el 21 de junio hasta el 20 de 
septiembre (incluidos) 
Desde el 21 de septiembre hasta el 20 de 
diciembre (incluidos)

Estación en el hemisferio norte:
Invierno, primavera, verano, otoño

Estación en el hemisferio norte:
verano, otoño, invierno, primavera

Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano."""

# Pedir al usuario el hemisferio, el mes y el día
hemisferio = input("¿En qué hemisferio te encuentras? N para norte y S para sur: ").strip().upper()
mes = int(input("Introduce el numero de mes (1-12): "))
dia = int(input("Introduce el día (1-31): "))

# Validar la estación según el hemisferio y la fecha
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación correspondiente es: {estacion}")

















