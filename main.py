import time

print("|-------------------------------------------|")
print("|                                           |")
print("|       Seja bem vindo a Pythônica!!        |")
print("|                                           |")
print("|                                           |")
print("|-------------------------------------------|")

print("Para seguir na plataforma, informe o seu nome.")
qtd_min_caracteres = int(3)## qtd minima de caracteres para o nome
tentativas_nome = 1
nome = False

while True:
    nome_usuario = input("Nome:")

    if len(nome_usuario)> qtd_min_caracteres and nome_usuario.isalpha(): ##isalpha(verifica se todos os caracteres são letras)
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
validacao_contato =  False

if nome == True:
    while tentativas_opcoes < 3:
        print(f"Olá {nome_usuario}, selecione uma das opcoes:")
        print("[1] = Cadastrar novo contato\n[2] = Visualisar todos os contatos\n[3] = Sair")

        try:
            opcoes = int(input("Opção:"))

            if(opcoes == 1):
                cadastrar_contatos = True
                break
                
            elif(opcoes == 2):
                print("Vizualizar todos os contatos")

            elif(opcoes == 3):
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

    if(cadastrar_contatos):
        qtd_min_caracteres_contato = int(3)
        nome_contato = input("Nome:")
                
        telefone_contato = int(input("Telefone:"))
        email_contato = input("E-mail:")

        if len(nome_contato) > qtd_min_caracteres_contato and nome_contato.isalpha(): # validação nome do contato se é > 3 e que seja apenas caracteres tipo texto
            validacao_contato = True
            print("Nome do contato esta correto")

        else:
            print("Informe um nome com mais de 3 caracteres")    

        if(len(str(telefone_contato)) > 8 and len(str(telefone_contato)) < 15 ):#Verifico se o contato é entre 8 e 15
            print("Passou no teste do contato")

        else:
            print("Informe um número de telefone correto")   

        if("@" in email_contato and ".com" in email_contato):## Vejo se @ e .com estão no texto que o usuário digitou
            print("e-mail válido")

        else:
            print("E_mail inválido")


                
      
  



