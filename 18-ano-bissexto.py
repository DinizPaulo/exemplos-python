import os 
os.system("cls")

ano = int(input("EM QUAL ANO ESTAMOS? "))

if (ano % 4 == 0):
    print("ANO BISSEXTO!")

else:
    print("NÃO É ANO BISSEXTO!")