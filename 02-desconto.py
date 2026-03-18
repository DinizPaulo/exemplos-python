import os 

os.system("cls")

#1 Passo - Variaveis e Entradas
print("Calculadora de Descontos")

nome_produto = input("Entre com o nome do produto: ")
preco = float(input("Entre com o preço do produto: "))
percentual_desconto = float(input("Entre com o percentual do desconto %: "))

#2 Passo - Processamento 
valor_desconto  = preco * percentual_desconto / 100
preco_final = preco - valor_desconto

#3 Passo - Exibir a saída
print("===========================================")
print("Preço original: ", preco, " - Preço com Desconto: ", preco_final)
print(f"Preço Original : R$ {preco} - Preço com Desconto: R$ {preco_final}")