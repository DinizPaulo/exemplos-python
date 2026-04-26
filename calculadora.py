import os 
os.system("cls")

while True:
    print("Calculadora Simples")

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))  

    def soma(num1,num2):
            soma = num1 + num2
            print(f"A soma de {num1} + {num2} é: {soma}")

    def subtracao(num1,num2):
            subtracao = num1 - num2
            print(f"A subtração de {num1} - {num2} é: {subtracao}")

    def multiplicacao(num1,num2):
            multiplicacao = num1 * num2
            print(f"A multiplicação de {num1} * {num2} é: {multiplicacao}")

    def divisao(num1,num2):
            if num2 != 0:
                divisao = num1 / num2
            print(f"A divisão de {num1} / {num2} é: {divisao}")
        
                    
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = int(input("Digite o número da operação desejada: "))
            

    if escolha == 1:
                soma(num1,num2)
            
    elif escolha == 2:
                subtracao(num1,num2)

    elif escolha == 3:
                multiplicacao(num1,num2)

    elif escolha == 4:
                divisao(num1,num2)

    elif escolha == 5:
                print("Encerrando a calculadora. Até mais!")

    else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                
    continuar = input("Deseja realizar outra operação? (s/n): ")

    if continuar.lower() == 's':
                os.system("cls")
    
    else:    print("Encerrando a calculadora. Até mais!")