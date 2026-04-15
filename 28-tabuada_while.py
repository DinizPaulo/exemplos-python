import os
os.system("cls")

print("SUPER TABUADA.WHILE")

# META: criar uma tabuada usando while, função sendo utilizada somente agora no curso

# entrada de dados 
numero =  int(input("Digite um número: "))
intervalo = int(input("Digite o fim do intervalo: "))


contador = 0 

#processamento e saída 
while (contador <= intervalo):
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1