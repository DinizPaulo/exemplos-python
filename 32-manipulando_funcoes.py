import funcoes

print("Manipulando funções com Python")

resposta = "S"

while(resposta == "S"):

    funcoes.limpar_tela()
    
    # Chamando a função exibir_menu
    funcoes.exibir_menu() 

    opcao = int(input("Escolha uma das opções: "))

    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if (opcao == 1):
        #chamar a opção somar
        total = funcoes.somar(numero1, numero2)
        print(f"A Soma é: {total}")
    elif (opcao == 2):
        #chamar a opção subtrair
        print(f"A Subtração é {funcoes.subtrair(numero1, numero2)}")
    elif (opcao == 3):
        #chamar a opcao Multipilcar
        print(f"A Multiplicação é {funcoes.multiplicar(numero1, numero2)}")

    elif (opcao == 4):
        #chamar a opcao Dividir
        print(f"A Divisão é {funcoes.dividir(numero1, numero2)}")

    else:
        print("Operação inválida!")

    resposta = input("Deseja realizar outra operação? (S/N): ").upper()
