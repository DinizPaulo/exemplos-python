import os 
os.system("cls")

nome = input("Por favor informe seu nome: ")
peso = float(input("Informe seu peso: "))
altura = int(input("Informe sua altura em cm: "))
ano_nascimento = int(input("Informe sua ano de nascimento: "))

idade = 2026 - ano_nascimento
peso_apto = peso >= 50
idade_apta = idade >= 18 and idade <= 65

texto_saida = (f"\tNOME: {nome}\n\tIDADE: {idade} anos\n\tPESO: {peso} kg\n\tALTURA: {altura} cm \n\tAPTO PARA DOAÇÃO: {'Sim' if peso_apto and idade_apta  else 'Não'}")

print(texto_saida)