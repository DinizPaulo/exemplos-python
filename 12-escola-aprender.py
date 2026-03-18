import os
os.system("cls")

nivel = int(input("QUAL O NÍVEL DO PROFESSOR DE 1 A 3 "))
aulas = int(input("QUANTAS AULAS O PROFESSOR LECIONOU? "))

if(nivel == 1):
    valor_aula = 12

elif(nivel == 2):
    valor_aula = 17

elif(nivel == 3):
    valor_aula = 25

else:
    print("NÍVEL INVALIDO!")
    valor_aula = 0

salario = valor_aula * aulas * 4 

print("\n---RESULTADO---")
print(f"Saláio final: R$ {salario}")
