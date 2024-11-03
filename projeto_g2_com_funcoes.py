import time

def boas_vindas():
    print("|----------------------------------------------------------------------------------|")
    print("|                                                                                  |")
    print("|                         Seja bem vindo a Pythônica!!                             |")
    print("|                                                                                  |")
    print("|                                                                                  |")
    print("|----------------------------------------------------------------------------------|")

qtd_min_caracteres_nome = int(3)# Qtd de caracteres para o nome
tentativas_nome = 1
nome = False

def validacao_nome_usuario():
    global tentativas_nome
    global nome
    global nome_usuario

    print("Para seguir na plataforma, informe o seu nome.")
    while True:
        nome_usuario = input("Nome:").strip()
        print("-----------------------------------------")
        if len(nome_usuario)> qtd_min_caracteres_nome and nome_usuario.replace(" ", "").isalpha(): ##isalpha(verifica se todos os caracteres são letras)
            nome = True
            time.sleep(0.70)
            break
        elif(tentativas_nome == 3):
            print("Quantide de tentativas excedida.")
            break
        else:
            print(f"Informe mais de 3 caracteres. Tentativa {tentativas_nome} de 3")
            tentativas_nome = tentativas_nome + 1  
tentativas_opcoes = 0
cadastrar_contatos = False

def opcoes_menu():
    global tentativas_opcoes
    global cadastrar_contatos
    if nome == True:
        while tentativas_opcoes < 3:
            print(f"Olá {nome_usuario}, selecione uma das opcoes:")
            print("[1] = Cadastrar novo contato\n[2] = Sair")

            try:
                opcoes = int(input("Opção:"))
                print("-----------------------------------------")

                if(opcoes == 1):
                    cadastrar_contatos = True
                    break

                elif(opcoes == 2):
                    time.sleep(0.80)
                    print("Saindo...") 
                    exit()

                else:
                    tentativas_opcoes += 1
                    print(f"-------- Tentativa {tentativas_opcoes} de 3----------")

            except ValueError:
                print("Opção invalida. Informe uma das opções motradas à cima")
                tentativas_opcoes += 1
                print(f"-------- Tentativa {tentativas_opcoes} de 3----------")


boas_vindas()
validacao_nome_usuario()
opcoes_menu()
