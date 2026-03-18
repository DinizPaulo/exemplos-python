import os 
os.system("cls")

nome_produto = input("Qual o nome do produto? ")
quantidade_produto = int(input("Qual a quantidade adquirida do produto? "))
precouni_produto = float(input("Qual o preço unitario do produto? "))

total = quantidade_produto * precouni_produto

if(quantidade_produto <= 5):
    desconto = total * 0.02

elif(quantidade_produto > 5 and quantidade_produto <= 10):
    desconto = total * 0.03
else:
    desconto = total *0.05

total_a_pagar = total - desconto

print("\n---RESULTADO---")
print(F"PRODUTO{nome_produto}")
print(f"TOTAL SEM DESCONTO: R$ {total}")
print(f"DESCONTO: R$ {desconto}")
print(f"TOTAL A PAGAR: R$ {total_a_pagar}")

