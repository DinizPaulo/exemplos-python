import os
os.system("cls")

def exibir_menu():
    print("[1] - REAL para Dolar")
    print("[2] - DOLAR para Real")
    print("[3] - Sair")

def converter_real_para_dolar(quantia_real, taxa_dolar):
    total_dolar = quantia_real / taxa_dolar
    return total_dolar

def converter_dolar_para_reais(quantia_dolar, taxa_real):
    total_reais = quantia_dolar * taxa_real
    return total_reais

def sair():
    input("Obrigado por utilizar o sistema, precione <ENTER> para sair...")
    exit()



while True:
    os.system("cls")
    print("Seja bem vindo ao conersor de moedas")

    #Chamando a função exibir_menu
    exibir_menu()

    opcao = int(input("Escolha uma opção: "))

    #Converter de Real para Dolar
    if (opcao == 1 ):
        print("=== Converção de Real para Dolar === ")
        quantia_real = float(input("Informe a quantia de reais: "))
        taxa_dolar = float(input("Informe a cotação do Dolar: "))
        
        total_dolar = converter_real_para_dolar(quantia_real,taxa_dolar)

        print(f"O total de dolares convertidos é: ${total_dolar}")
        print("Pressione <ENTER> para continuar")

    #Converter Dolar para Real
    elif(opcao == 2):
        print("=== Conversor de Dolar para Real ===")
        quantia_dolar = float(input("Informe a quantia de Dolar: "))
        taxa_real= float(input("Informe a cotação do real: "))

        total_reais = converter_dolar_para_reais(quantia_dolar, taxa_real)

        print(f"O total de reais convertido é: R${total_reais}")
        print("Pressione <ENTER> para continuar")

    #Sair 
    elif(opcao == 3):
        sair()