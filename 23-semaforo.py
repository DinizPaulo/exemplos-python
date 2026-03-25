import os 
os.system("cls")

cor = input("QUAL A COR DO SEMÁFORO? ")

cor1 = "Verde" 
cor2 = "Amarelo" 
cor3 = "Vermelho" 

if (cor == cor1):
    print("Pode passar!")

elif (cor == cor2):
    print("Atenção!")

elif (cor == cor3):
    print("Não pode passar!")

else:
    print("Não existe essa cor no semáforo!")