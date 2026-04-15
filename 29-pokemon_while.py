import os
import random
import time

os.system("cls")

# Criar um sistema de batalha Pokémon usando Python, aplicando estruturas de decisão (if, elif, else) e repetição (while)
#Objetivo: Desenvolver lógica de programação na prática, simulando um jogo real
#Regras do desafio
#- O jogo deve ter:
#- Vida do jogador e do inimigo
#- Menu com opções (Atacar, Curar, Fugir)
#- Sistema de turnos
#- Condição de vitória e derrota

print("BEM VINDO A BATALHA POKEMON!")
print("====================================")

#Entrada de dados, escolha dos pokemons e nome do treinador pokemon.

nome = input("INFORME SEU NOME: ")

vida_jogador = 50
vida_inimigo = 50

while (vida_jogador > 0 or vida_inimigo > 0):
    os.system("cls")
    print(f"Vida {vida_jogador} | Vida inimigo {vida_inimigo}")
    print("FAÇA SUA JOGADA!")
    print("1-Atacar")
    print("2-Curar")
    print("3-Fugir")

    opc_jogador = int(input("Escolha uma opção: "))
    opc_inimigo = random.randint(1,3)

    #sua vez de jogar
    #atacou
    if(opc_jogador == 1 ):
        print("Você escolheu atacar")
        time.sleep(3)
        vida_inimigo -= 10

    #defendeu
    elif(opc_jogador == 2 ):
        print("Você escolheu se defender")
        time.sleep(3)
        vida_jogador += 5

    #fugir
    elif(opc_jogador == 3 ):
        print("Você fugiu")
    
        print("Jogada encerrada...")
        time.sleep(3)
        print("Iniciando a jogdada do inimigo em 3 segundos")

    #vez do seu inimigo
    if(opc_inimigo == 1):
            print("o inimigo escolheu atacar: ")
            time.sleep(3)
            vida_jogador -= 10

    if(opc_inimigo == 2):
            ("o inimigo escolheu curar: ")
            time.sleep(3)
            vida_inimigo += 5

    if(opc_inimigo == 3):
            time.sleep(3)
            print("Seu inimigo fugiu!")

    print("Jogada encerrada...")
    time.sleep(3)
# verificando a vida
            
if (vida_jogador > vida_inimigo):
    print("Parabens você venceu!")

else:
    print("Você perdeu!")