import os
import historia_mini_game
import time
os.system("cls")

print("*******************************************")
print("**      Welcome to the Mini Game!        **")
print("*******************************************")


while True:   

    print("\nVocê acordou em uma floresta misteriosa. Você tem duas opções: ")
    print("1 - Seguir o caminho à esquerda")
    print("2 - Seguir o caminho à direita")
    print("3 - Sair do Jogo")
        
    escolha = int(input("Digite o número da sua escolha: "))
        
    if escolha == 1:
        historia_mini_game.esquerda()

    elif escolha == 2:
        historia_mini_game.direita()   

    elif escolha == 3:
        print("Encerrando o jogo. Até mais!")
    else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    