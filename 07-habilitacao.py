import os
os.system("cls")

# 1 etapa - entrada
print("Atividade - Habilitação")

idade =int(input("Digite sua idade: "))

if(idade >= 18):
    habilitacao = input("Possui Habilitação (Sim) ou (Não) ").upper()

    print("Você pode dirigir!")

    if(habilitacao == "SIM"):
        print("Você pode dirigir! ")
    else:
        print("Você não possui habilitação para dirigir! ")

