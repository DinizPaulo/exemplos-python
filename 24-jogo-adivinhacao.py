import os 
os.system("cls")

import random

numero_sorteado = random.randint (1,10)

print("BEM VINDO AO SEU JOGO DA ADVINHAÇÃO!")
print("===================================================")
palpite = int(input("DIGITE UM NUMERO DE 1 A 10 "))

if (palpite == numero_sorteado):
    print("ACERTOU!")

elif (palpite < 1 or palpite > 10):
    print("Esse palpite está invalido")

else:
    print(f"Errou, o numero era {numero_sorteado}!")
