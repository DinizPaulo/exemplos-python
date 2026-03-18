import os
os.system("cls")

# 1 etapa - entrada
print("Calculadora de idade")
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# 2 etapa - processamento
idade = ano_atual - ano_nascimento
print(f"Você tem {idade} anos de idade")