""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos: 
● Posición lista_anidada[0]: 15 
● Posición lista_anidada[1]: True 
● Posición lista_anidada[2][0]: 25.5 
● Posición lista_anidada[2][1]: 57.9 
● Posición lista_anidada[2][2]: 30.6 
● Posición lista_anidada[3]: False 
Imprimir la lista resultante por pantalla. """

lista_anidada = []

lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([])
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9)
lista_anidada[2].append(30.6)
lista_anidada.append(False)

print(lista_anidada)