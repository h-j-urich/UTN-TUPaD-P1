"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla: 
● Menor que 3: "Muy leve" (imperceptible). 
● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
generalmente no causa daños). 
● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
débiles). 
● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).  """

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Magnitud muy leve(imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Magnitud leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Magnitud moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Magnitud fuerte (puede causar daños en estructuras debiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Magnitud muy fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Magnitud extremo (puede causar daños graves a gran escala)")

