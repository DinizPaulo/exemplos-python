import os 
os.system("cls")

print("Exemplo com while - Salário do professor")

while True:
    os.system("cls")

    print("===MENU===")
    print("1 - Calcular Salário")
    print("2 - Sair")

    opcao = int(input("Escolha uma opção: "))

    #Verificando a opção escolhida
    if (opcao == 1):
        os.system("cls")

        print("Qual o nível do professor? ")
        print("1 - Professor Nível I")
        print("2 - Professor Nível II")
        print("3 - Professor Nível III")
       
        nivel = int(input("Escolha um nível: "))

        if (nivel >= 4):
            print("Nível inválido!")
            input("Pressione <Enter> para continuar...")
            continue 
        else:
            qtd_aulas = int(input("Informe a qtd de aulas mensais: "))
            
        if (nivel == 1):
            salario = qtd_aulas * 12.00
        elif (nivel == 2):            
            salario = qtd_aulas * 17.00  
        elif (nivel == 3):
            salario = qtd_aulas * 25.00
        else:
            print("Nível inválido!")
            input("Pressione <Enter> para continuar...")
            continue 
        
        print(f"O salário do professor é: R${salario}")

        input("Pressione <Enter> para continuar")

    elif (opcao == 2):
        input("Pressione <Enter> para sair do programa...")
        break

print("Finalizou o programa!")