import os 
os.system("cls")

peso = float(input("QUAL SEU PESO? "))
altura = float(input("QUAL SUA ALTURA?"))

imc = peso / (altura ** 2)

if(imc <16.9):
    print("Muito abaixo do peso")

elif(imc >= 17 and imc < 18.4):
    print("Abaixo do peso")

elif(imc > 18.5 and imc < 24.9):
    print("Peso normal")

elif(imc >= 25 and imc < 29.9):
    print("Acima do peso")

elif(imc >= 30 and imc < 34.9):
    print("Obesidade grau 1")

elif(imc >= 35 and imc < 40):
    print("Obesidade grau 2")

else:
    print("Obesidade grau 3")
