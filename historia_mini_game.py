import time

#============= PARTE ESQUERDA =============
def esquerda():
    print("\nVocê seguiu o caminho à esquerda e encontrou uma tribo amigável. Eles te convidaram para um banquete.")
    time.sleep(2)
    print("Escolha uma das opções... ")
    time.sleep(1)
    print("1 - Aceitar o convite e participar do banquete")
    time.sleep(1)
    print("2 - Recusar o convite e seguir em frente")
    time.sleep(1)
    escolha_banquete = int(input("Digite o número da sua escolha: ")) 

    if escolha_banquete == 1:
        aceitou() 
    elif escolha_banquete == 2:
        recusou()
   
  
def aceitou():
        print("\nEscolha uma da opções...")
        time.sleep(2)
        print("1 - Ficar mais um pouco no banquete e aproveitar a festa")
        time.sleep(1)
        print("2 - Se despedir e seguir em frente")
        time.sleep(1)
        pos_festa = int(input("Digite o número da sua escolha: ")) 

        if pos_festa == 1:
            ficou_bebado()
        
        elif pos_festa == 2:
            seguiu_em_frente() 
          
def ficou_bebado():
        print("\nEscolha uma da opções: ")
        time.sleep(2)
        print("1 - Tentar encontrar um lugar para descansar e se recuperar")
        time.sleep(1)
        print("2 - Continuar caminhando pela floresta mesmo estando bêbado")
        time.sleep(1)
        escolha_bebado = int(input("Digite o número da sua escolha: ")) 

        if escolha_bebado == 1:
            print("\nVocê encontra um lugar seguro para descansar, mas acaba sendo atacado por animais selvagens. GAME OVER.")  

        elif escolha_bebado == 2:
            print("\nVocê continua caminhando pela floresta, mas acaba se perdendo e não consegue encontrar o caminho de volta. GAME OVER.") 
        
def seguiu_em_frente():
     time.sleep(2)
     print("\nVocê segue em frente, mas acaba se perdendo na floresta. GAME OVER.")

def recusou():
        print("\nEscolha uma da opções: ")
        time.sleep(2)
        print("1 - Tentar negociar com a tribo para ser libertado")
        time.sleep(1)
        print("2 - Tentar fugir da tribo")
        time.sleep(1)
        escolha_refem = int(input("Digite o número da sua escolha: ")) 

        if escolha_refem == 1:
            print("\nVocê tenta negociar com a tribo, mas eles não querem ouvir e continuam te mantendo como refém.")   
            negociar()

        elif escolha_refem == 2:
            print("\nVocê tenta fugir da tribo, mas eles são rápidos e conseguem te capturar novamente.")
            fugir()

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def negociar():
        time.sleep(2)
        print("\nVocê tenta negociar com a tribo, mas eles não querem ouvir e continuam te mantendo como refém. GAME OVER.")

def fugir():
        time.sleep(2)
        print("\nVocê tenta fugir da tribo, mas eles são rápidos e conseguem te capturar novamente. GAME OVER.")

# ============= PARTE DIREITA =================

def direita():
            
    print("\nVocê seguiu o caminho à direita e não encontoru nada de interessante. Você continua caminhando e acaba se perdendo na floresta.")
    time.sleep(2)
    print("Escolha uma da opções: ")
    time.sleep(1)
    print("1 - Acampar perto de um rio calmo e esperar o amanhecer")
    time.sleep(1)
    print("2 - Continuar caminhando floresta a dentro")
    time.sleep(1)
    escolha_perdido = int(input("Digite o número da sua escolha: ")) 

    if escolha_perdido == 1:
        print("\nVocê acampa perto do rio e passa a noite em segurança.")
    elif escolha_perdido == 2:
        print("\nVocê continua caminhando pela floresta, e encontra uma cabana velha.")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

def acampou():
        print("\nEscolha uma da opções: ")
        time.sleep(2)
        print("1 - Atravesar o rio, assim que amanhece para explorar a outra margem")
        time.sleep(1)
        print("2 - Continuar camihando pela floresta a de manhã, mesmo estando perdido")
        time.sleep(1)
        escolha_rio = int(input("Digite o número da sua escolha: ")) 

        if escolha_rio == 1:
            print("\nVocê atravesa o rio e explora a outra margem, e encontra uma caverna misteriosa...")
            atravesar_rio()

        elif escolha_rio== 2:
            print("\nVocê fica acampado e espera mais um dia, e de noite ouve sons estranhos...")
            continuar_caminhando()

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def atravesar_rio():
        print("\nVocê atravessa o rio e explora a outra margem, e encontra uma caverna misteriosa...")
        time.sleep(1)
        print("1 - Entrar na caverna para investigar")
        time.sleep(1)
        print("2 - Ignorar a caverna e continuar explorando a outra margem")
        time.sleep(1)
        escolha_caverna = int(input("Digite o número da sua escolha: "))

        if escolha_caverna == 1:
            print("\nVocê entra na caverna e encontra um tesouro escondido. Parabéns, você venceu o jogo e descobriu o final secreto!")

        elif escolha_caverna == 2:
            print("\nVocê ignora a caverna e continua explorando, mas acaba se perdendo novamente na floresta. GAME OVER.")


def continuar_caminhando():
        print("\nVocê continua caminhando pela floresta, e encontra um urso.")
        time.sleep(2)
        print("1 - Tentar se esconder e esperar o urso ir embora")
        time.sleep(1)
        print("2 - Tentar enfrentar o urso para se defender")
        time.sleep(1)
        escolha_urso = int(input("Digite o número da sua escolha: "))

        if escolha_urso == 1:
            print("\nVocê se esconde atrás de uma árvore, mas o urso te encontra e te ataca. GAME OVER.")

        elif escolha_urso == 2:
            print("\nVocê enfrenta o urso com coragem, mas infelizmente ele é muito forte e te derrota. GAME OVER.")
    
def caminhou():
        print("\nEscolha uma da opções: ")
        time.sleep(2)
        print("1 - Entrar na cabana velha para procurar por suprimentos")
        time.sleep(1)
        print("2 - Ignorar a cabana e continuar caminhando pela floresta")
        time.sleep(1)
        escolha_cabana = int(input("Digite o número da sua escolha: ")) 

        if escolha_cabana == 1:
            print("\nVocê entra na cabana e encontra um velho com uma arma na mão...")
            velho()

        elif escolha_cabana == 2:
            print("\nVocê ignora a cabana e continua caminhando, mas acaba se perdendo ainda mais na floresta. GAME OVER.")
            ignorar_cabana()
            
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.") 

def velho():
        print("\nVocê entra na cabana e encontra um velho com uma arma na mão...")
        time.sleep(2)
        print("1 - Tentar conversar com o velho para descobrir suas intenções")
        time.sleep(1)
        print("2 - Tentar atacar o velho para se defender")
        time.sleep(1)
        escolha_velho = int(input("Digite o número da sua escolha: "))

        if escolha_velho == 1:
            print("\nVocê tenta conversar com o velho, mas ele é hostil e te ataca. GAME OVER.")

        elif escolha_velho == 2:
            print("\nVocê tenta atacar o velho, mas ele tem uma arma e te derrota. GAME OVER.")

def ignorar_cabana():
        time.sleep(2)
        print("\nVocê ignora a cabana e continua caminhando, mas acaba se perdendo ainda mais na floresta. GAME OVER.")
