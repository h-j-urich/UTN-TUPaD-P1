""" escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. """

import random
from statistics import  mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

#calcular la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#determinar el tipo de sesgo

if media > mediana > moda:
    sesgo = "Sesgo positivo"
elif media < mediana < moda:
    sesgo = "Sesgo negativo"
else:
    sesgo = "Sin sesgo"

print("Lista de numero aleatorios", numeros_aleatorios)
print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)
print("Resultado del sesgo: ", sesgo)