import os
os.system("cls")

import time


def exibir_menu():
    print("[1] - Dividir conta")
    print("[2] - Sair")


def pagamento():
    print("[1] - Dinheiro")
    print("[2] - Cartão")
    print("[3] - VR")


def sair():
    print("Obrigado por utilizar nosso sistema!")
    exit()


def efetuar_pagamento_dinheiro(valor_conta, quantidade_pessoas):

    taxa_pagamento = 0
    subtotal = valor_conta + taxa_pagamento

    taxa_garcom = subtotal * 0.10

    valor_total = subtotal + taxa_garcom

    valor_por_pessoa = valor_total / quantidade_pessoas

    return taxa_pagamento, taxa_garcom, valor_total, valor_por_pessoa


def efetuar_pagamento_cartao(valor_conta, quantidade_pessoas):

    taxa_pagamento = valor_conta * 0.03
    subtotal = valor_conta + taxa_pagamento

    taxa_garcom = subtotal * 0.10

    valor_total = subtotal + taxa_garcom

    valor_por_pessoa = valor_total / quantidade_pessoas

    return taxa_pagamento, taxa_garcom, valor_total, valor_por_pessoa


def efetuar_pagamento_vr(valor_conta, quantidade_pessoas):

    taxa_pagamento = valor_conta * 0.02
    subtotal = valor_conta + taxa_pagamento

    taxa_garcom = subtotal * 0.10

    valor_total = subtotal + taxa_garcom

    valor_por_pessoa = valor_total / quantidade_pessoas

    return taxa_pagamento, taxa_garcom, valor_total, valor_por_pessoa


while True:

    os.system("cls")
    print("==== DIVISOR DE CONTA ====")

    exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    if (opcao == 1):

        print("Dividindo conta...")

        valor_conta = float(input("Digite o valor da conta: R$ "))
        quantidade_pessoas = int(input("Digite a quantidade de pessoas: "))

        pagamento()

        opcao_pagamento = int(input("Escolha uma opção de pagamento: "))

        if (opcao_pagamento == 1):

            taxa, garcom, total, por_pessoa = efetuar_pagamento_dinheiro(
                valor_conta,
                quantidade_pessoas
            )

            print("\n===== RESUMO =====")
            print(f"Valor original: R$ {valor_conta:.2f}")
            print(f"Taxa pagamento: R$ {taxa:.2f}")
            print(f"Taxa garçom: R$ {garcom:.2f}")
            print(f"Valor total: R$ {total:.2f}")
            print(f"Valor por pessoa: R$ {por_pessoa:.2f}")

            time.sleep(5)

        elif (opcao_pagamento == 2):

            taxa, garcom, total, por_pessoa = efetuar_pagamento_cartao(
                valor_conta,
                quantidade_pessoas
            )

            print("\n===== RESUMO =====")
            print(f"Valor original: R$ {valor_conta:.2f}")
            print(f"Taxa pagamento: R$ {taxa:.2f}")
            print(f"Taxa garçom: R$ {garcom:.2f}")
            print(f"Valor total: R$ {total:.2f}")
            print(f"Valor por pessoa: R$ {por_pessoa:.2f}")

            time.sleep(5)

        elif (opcao_pagamento == 3):

            taxa, garcom, total, por_pessoa = efetuar_pagamento_vr(
                valor_conta,
                quantidade_pessoas
            )

            print("\n===== RESUMO =====")
            print(f"Valor original: R$ {valor_conta:.2f}")
            print(f"Taxa pagamento: R$ {taxa:.2f}")
            print(f"Taxa garçom: R$ {garcom:.2f}")
            print(f"Valor total: R$ {total:.2f}")
            print(f"Valor por pessoa: R$ {por_pessoa:.2f}")

            time.sleep(5)

        else:
            print("Opção inválida!")
            time.sleep(2)

    elif (opcao == 2):
        sair()

    else:
        print("Opção inválida!")
        time.sleep(2)