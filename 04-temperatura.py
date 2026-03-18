import os
os.system("cls")

# 1 etapa - entrada

print("Seja bem vindo ao seu Conversor de Temperatura")

Celsius = float(input("Digite o clima atual em Celsius: "))

# 2 etapa - processamento
Fahrenheit = (9*Celsius + 160) / 5 

# 3 etapa - saída
print(f"O valor em Fahrenheit é: {Fahrenheit}")
