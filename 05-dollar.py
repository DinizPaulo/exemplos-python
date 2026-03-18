import os
os.system("cls")

# 1 etapa - entrada
print("Conversor de Dollar para Reais: ")

Dollar = float(input("Digite a quantidade de dollar: "))
cotacao_dollar = float(input("Digite a cotação do dollar hoje: "))

# 2 etapa - processamento
total_reais = Dollar * cotacao_dollar

# 3 etapa - saída 
print(f"O total em reais é R$ {total_reais:.2f}")