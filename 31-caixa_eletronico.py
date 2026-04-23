import os
os.system("cls")



print("Bem-vindo ao Seu Caixa Eletronico")

while True:

    print("O que você deseja fazer?")
    print("1-Depositar")
    print("2-Sacar")
    print("3-Conferir Saldo")
    desejo = int(input("Escolha a operação: "))


    saldo = float ()

    if desejo == 1:
        deposito = float(input("Quanto você deseja depositar: "))
        saldo_atual = saldo + deposito 
        print(f"Esse é seu saldo atual: {saldo_atual}")

    elif desejo == 2:
        saque = float(input("Qual o valor que você deseja sacar: "))
        saldo_atual = saldo - saque
        print(f"Esse é seu saldo atual: {saldo_atual}")

    elif desejo == 3:
        print(saldo)

    else:
        print("Operação invalida!")
        break 

    continuar = input("Deseja continuar a utilizando o caixa eletronico? S/N").upper()

    if continuar == "S":
        input("Precione <ENTER> para continuar")
        continue

    else:
        break