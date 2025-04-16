"""  9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
 una temperatura en grados Celsius y devuelva su equivalente en
 Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
 resultado usando la función."""

def celsius_a_fahranheit(celsius):
    return (celsius * 1.8) + 32
    

solicitar_grados = float(input("Ingrese la temperatura en grados Celsius: "))

grados_fahrenheit = celsius_a_fahranheit(solicitar_grados)

print(f"La temperatura {solicitar_grados} grados Celsius es equivalente a {grados_fahrenheit} grados Fahrenheit.")
