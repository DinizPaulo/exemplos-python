import os 
os.system("cls")

veiculo = input("QUAL É O SEU VEICULO? ")

carro = "Carro"
moto = "Moto"
caminhao = "Caminhão"

if (veiculo == carro):
    print("Você deve pagar R$10,00 de pedágio")

elif (veiculo == moto):
    print("Você devera pagar R$5,00 de pedágio")

elif (veiculo == caminhao):
    print("Você devera pagar R$20,00 de pedágio")

else:
    print("Esse veiculo não existe ou não paga pedágio")