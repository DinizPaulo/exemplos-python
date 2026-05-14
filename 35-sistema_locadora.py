import os 

# =================================
# Ver catálogo
# =================================
def exibir_catalogo(filmes):
    os.system("cls")
    print("==== CATÁLOGO DE FILMES ====")

    for item in filmes:
        print(f"Titulo: {item["titulo"]}")
        print(f"Gênero: {item["genero"]}")
        print("-" * 30)

# =================================
# Carregar Menu do Admin
# =================================
def carregar_menu_admin():
    os.system("cls")
    print("==== Autenticação ====")
    usuario = input("Informe seu usuário: ")
    senha = input("Informe sua senha: ")

    if usuario != "admin" and senha != "123":
        input("Acesso negado!")
        return

    while True:
        os.system("cls")
        print("==== MENU DO ADMINISTRADOR ====")
        print("[1] - Cadastrar filme")
        print("[2] - Ver catálogo")
        print("[3] - Top e Flop")
        print("[4] - Voltar")

        op = int(input("Escolha uma opção: "))

        if op == 1:
            os.system("cls")
            print("==== Cadastro de filme ====")
            titulo = input("Informe o título do filme: ")
            genero = input("Informe o gênero do filme: ")

            filme = {
                "titulo": titulo,
                "genero": genero,
                "avaliacoes": [],
                "media": 0,
                "classificacao": "Sem Classificação",
                "disponivel": True,
                "cliente": None
            }
            filmes.append(filme)
            print("Filme cadastrado com sucesso!")
            input("Pressioner <ENTER> para continuar...")

        elif op == 2:
            exibir_catalogo(filmes)
            input("Pressione <ENTER> para continuar...")

        elif op == 4:
            break
            
        else:
            print("Opção inválida!")
            input("Pressione <ENTER> para continuar...")

# =================================
# Sistema principal
# =================================
os.system("cls")

# Lista de filmes (banco de dados)
filmes = []

while True:
    os.system("cls")
    print("==== BEM VINDO A LOCADORA CINEFLIX ====")
    print("[1] - Entrar como cliente")
    print("[2] - Entrar como administrador")
    print("[3] - Sair")
    op = int(input("Escolha uma opção: "))

    if op == 1:
        print("Entrou como cliente")

    if op == 2:
        print("Entrou como administrador")
        carregar_menu_admin()

    if op == 3:
        print("Obrigado por usar o sistema!")
        input("Pressione <ENTER> para sair...")
        break