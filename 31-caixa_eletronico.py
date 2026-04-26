import os
os.system("cls")

saldo = 1000.0

print("Bem-vindo ao Seu Caixa Eletronico")

while True:

    print("O que você deseja fazer?")
    print("1-Depositar")
    print("2-Sacar")
    print("3-Ver Saldo")
    desejo = int(input("Escolha a operação: "))

    if desejo == 1:
        deposito = float(input("Quanto você deseja depositar: "))
        
        if deposito > 0:
            saldo += deposito
        print(f"Operação realizada com sucesso!")

    elif desejo == 2:
        saque = float(input("Qual o valor que você deseja sacar: "))
        if saque > 0 and saque <= saldo:
            saldo -= saque
            print(f"Operação realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    elif desejo == 3:
        print(f"Seu saldo é: {saldo}")

    else:
        print("Operação invalida!")
        break 

    continuar = input("Deseja continuar a utilizando o caixa eletronico? S/N ").upper()

    if continuar == "S":
        input("Precione <ENTER> para continuar")
        continue

    else:
        break
