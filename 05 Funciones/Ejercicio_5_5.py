"""  5. Crear una función llamada segundos_a_horas(segundos) que reciba
 una cantidad de segundos como parámetro y devuelva la cantidad
 de horas correspondientes. Solicitar al usuario los segundos y mos
trar el resultado usando esta función."""

def segundos_a_horas(segundos):
    return segundos / 3600  # 3600 segundos en una hora

segundos_solicitados = int(input("Ingrese la cantidad de segundos: "))

horas = segundos_a_horas(segundos_solicitados)

print(f"{segundos_solicitados} segundos equivalen a {horas:.2f} horas")
