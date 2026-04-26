import os 
os.system("cls")

alunos={}

while True:

    print("Bem-vindo ao Sistema Academico")
    print("O que você deseja fazer?")
    print("""1-Cadastrar Aluno\n2-Listar Aluno\n3-Remover Aluno\n4-Sair""")

    opcao = int(input("Escolha a operação: "))

    if opcao == 1:
        nome = input("Digite o nome do aluno: ").capitalize()
        alunos[nome] = True
        print(f"Aluno {nome} cadastrado com sucesso!")
        input("Pressione <ENTER> para continuar")
        os.system("cls")

    elif opcao == 2:
        print("Listar de Alunos:")
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            for i, nome in enumerate(alunos):
                print(i, "-", nome)
        input("Pressione <ENTER> para continuar")
        os.system("cls")

    elif opcao == 3:
        print("Lista de Alunos:")
        for i, nome in enumerate(alunos):
            print(i, "-", nome)

        indice = int(input("Digite o indice do aluno que deseja remover: "))
            
        if indice >= 0 and indice < len(alunos):
            indice = int(indice)
            if 0 <= indice < len(alunos):
                aluno_removido = list(alunos.keys())[indice]
                del alunos[aluno_removido]
                print(f"{aluno_removido} removido com sucesso!")
            else:
                print("Número inválido.")
        else:
            print("Entrada inválida. Por favor, digite um número.")
        input("Pressione <ENTER> para continuar")
        os.system("cls")
    elif opcao == 4:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        input("Pressione <ENTER> para continuar")
        os.system("cls")