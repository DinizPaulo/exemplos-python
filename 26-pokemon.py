import os 
os.system("cls")

import random 

print("BEM VINDO AO SEU MINIGAME DE POKEMON!")

nome = input("Nome do Treinador: ")

print("=======================================================")

print("Você pode escolher um desses 3 pokemons")
print("=======================================================")
print("1-Charmander")
print("2-Squirtle")
print("3-Bulbasaur")

meu_pokemon = int(input("Escolha o pokemon de acordo com o numero indicado! "))

if (meu_pokemon == 1):
    print("Você escolheu o Charmander")

elif(meu_pokemon == 2):
    print("Você escolheu o Squirtle")

elif (meu_pokemon == 3):
    print("Você escolheu o Bulbasaur")

else:
    print("Esse pokemon não está na pokedash!")

pokemonpc = random.randint(1,3)

if (pokemonpc == 1):
    print("Seu inimigo o Charmander")

elif(pokemonpc == 2):
    print("Seu inimigo escolheu o Squirtle")

elif (pokemonpc == 3):
    print("Seu inimigo escolheu o Bulbasaur")

else:
    print("Esse pokemon não está na pokedash!")

# chamander vs charmander
if (meu_pokemon == 1 and pokemonpc == 1):
    print("Você empatou!")

# charmander vs squirtle
elif (meu_pokemon == 1 and pokemonpc == 2):
    print("Você perdeu, pois seu pokemon não é efetivo contra água!")
 
# charmander vs bulbasaur
elif (meu_pokemon == 1 and pokemonpc == 3):
    print("Você venceu, pois seu pokemon é efetivo contra plantas!")

# squirtle vs squirtle
elif (meu_pokemon == 2 and pokemonpc == 2):
    print("Você empatou!")

# squirtle vs charmander
elif (meu_pokemon == 2 and pokemonpc == 1):
    print("Você venceu, pois seu pokemon é efeitivo contra fogo!")

# squirtle vs bulbasaur
elif (meu_pokemon == 2 and pokemonpc == 3):
    print("Você perdeu, pois seu pokemon não efetivo contra plantas!")

# bulbasaur vs bulbasaur
elif (meu_pokemon == 3 and pokemonpc == 3):
    print("Você empatou!")

# bulbasaur vs charmander
elif (meu_pokemon == 3 and pokemonpc == 1):
    print("Você perdeu, pois seu pokemon não efetivo contra fogo!")

# bulbasaur vs squirtle
elif (meu_pokemon == 3 and pokemonpc == 2):
    print("Você venceu, pois seu pokemon é efeitivo contra água!")

else:
    print("Esse pokemon está na pokedash!")