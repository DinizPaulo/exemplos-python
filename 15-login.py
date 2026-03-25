import os 
os.system("cls")

user = "Admin"
password = "123"

usuario = input("NOME DO USUÁRIO: ")
senha = input("SENHA: ")

if (usuario == user and senha == password):
    print("Acesso liberado!")

else:
    print("Acesso negado!")