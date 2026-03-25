import os
os.system ("cls")

km = float(input("DIGITE A QUILOMETRAGEM RODADA: "))
gasolina = int(input("DIGITE QUANTOS LITROS DE GASOLINA VOCÊ UTILIZOU: "))

consumo = km / gasolina

print (f"ESSA É A MÉDIA DE KM POR LITRO QUE FOI GASTO: {consumo} KM/hr")