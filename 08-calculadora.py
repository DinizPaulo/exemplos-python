import os
os.system("cls")

print("Atividade Calculadora")

numero01 = float(input("Digite o primeiro numero: "))
numero02 = float(input("Digite o segundo numero: "))

print("Escolha uma das operações!")
print("+ - Adição")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")

operacao = input("Informe a operação:")

if(operacao == "+"):
    resultado = numero01 + numero02

elif(operacao == "-"):
    resultado = numero01 - numero02

elif(operacao == "*"):
    resultado = numero01 * numero02

elif(operacao == "/"):
    resultado = numero01 / numero02

else:
    print(" Operação invalida! ")

print("=" * 30)
print(f"operação escolhida: {operacao}")
print(f"resultado: {resultado}")





