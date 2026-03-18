import os 
os.system("cls")

#primeira etapa - entradas

print("Seja bem vindo ao boletim virtual")

nota01 = float(input("Entre com a primeira nota: "))
nota02 = float(input("Entre com a segunda nota: "))
nota03 = float(input("Entre com a terceira nota: "))

#segunda etapa - processamento
media = (nota01 + nota02 + nota03) / 3

if(media>=6):
    print("Você foi Aprovado!")

elif(media>= 4 and media <=5):
    print("O aluno está de recuperação!")
    
else:
    print("Você foi Reprovado!")

# terceira etapa - saída   
    print(f"Sua média foi {media}")