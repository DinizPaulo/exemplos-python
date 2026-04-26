import os 
os.system("cls")

def lista_candidatos(dict_candidatos):
    print("\n" *100)
    print("Candidatos: ")
    for numero, nome in dict_candidatos.items():
        print(numero, "-", nome)

def adiciona_candidato(dict_candidatos):
    lista_candidatos(dict_candidatos)
    print("\nInforme os dados do novo candidato")

    numero = (input("Número: "))
    nome = input("Nome: ")

    if len (numero) != 2 or not numero.isdigit() or numero in dict_candidatos:
        print("Número do candidato deve conter 2 dígitos.")
        return
    else:
        dict_candidatos[numero] = nome

def pegar_voto(dict_candidatos, dict_votos, voto):
    while True:
        lista_candidatos(dict_candidatos)
        print("\nInforme seu voto: ")
        voto = input("Informe o número do candidato: ").strip()
        if voto == "":
            voto = "branco"
        elif voto in dict_candidatos:
            voto = voto + " - " + dict_candidatos[voto]
        else:
            voto = "Nulo"
        print("Voto", voto)
        resposta = input("Confirma voto? (S/N): ").lower().strip()
        if resposta == "s":
            soma_voto(dict_votos, voto)
            break 

def soma_voto(dict_voto, voto ):
        if voto in dict_voto:
            dict_voto [voto] += 1
        else:
            dict_voto[voto] = 1

def principal():
        dict_candidatos = {}
        while True:
            adiciona_candidato(dict_candidatos)
            resposta = input ("Continuar cadastros (S/N): ").lower().strip()
            if resposta == "n":
             break
    
        dict_voto = {}
        total = 0 
        while True:
            (dict_candidatos, dict_voto)
            total += 1 
            resposta = input ("Encerra votação (S/N): ").lower().strip()
            if resposta == "s":
                break 
        print("RESULTADO DA ELEIÇÃO: ")
        for voto in dict_voto:
            porcentagem = round(dict_voto[voto] / total * 100, 2)
            print(voto, ": ", dict_voto[voto],
            ' (', porcentagem, '%', ')', sep='')
            
        if __name__== "__main__":
            principal()