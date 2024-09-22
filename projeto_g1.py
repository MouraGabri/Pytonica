import time
print("|----------------------------------------------------------------------------------|")
print("|                                                                                  |")
print("|                         Seja bem vindo a Pythônica!!                             |")
print("|                                                                                  |")
print("|                                                                                  |")
print("|----------------------------------------------------------------------------------|")

print("Para seguir na plataforma, informe o seu nome.")
qtd_min_caracteres = int(3)## qtd minima de caracteres para o nome
tentativas_nome = 1
nome = False

while True:
    nome_usuario = input("Nome:").strip()
    print("-----------------------------------------")
    if len(nome_usuario)> qtd_min_caracteres and nome_usuario.replace(" ", "").isalpha(): ##isalpha(verifica se todos os caracteres são letras)
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

    if(cadastrar_contatos):
        tentativas_contatos = 0
        qtd_de_contatos_cadastrados = 0
        total_contatos = 5
        contatos = [] 
        # Primeiro while externo para contar a qtd total de contatos cadastrados
        while  qtd_de_contatos_cadastrados < total_contatos:
            tentativas_contatos = 0 # Toda vez que ele completar um cadastro, zera o número de tentativas

            while tentativas_contatos < 3:# while interno para contar o número de tentativas
                qtd_min_caracteres_contato = int(3)
                nome_contato = input("Nome:")

                if len(nome_contato) > qtd_min_caracteres_contato and nome_contato.replace(" ", "").isalpha(): 
                    # validação nome do contato se é > 3 e que seja apenas caracteres tipo texto
                    break #Se passou ele vai para o próximo campo
                    
                else:
                    tentativas_contatos += 1
                    print(f"Informe apenas caracteres do tipo texto --- Tentativa {tentativas_contatos} de 3") 

                if tentativas_contatos == 3:
                    print("QTD de vezes atigingida")
                    exit()
                      
            while tentativas_contatos < 3:# while interno para contar o número de tentativas
                    telefone_contato = input("Telefone:")

                    if(len(telefone_contato) > 8 and len(telefone_contato) < 15  and  not telefone_contato.isalpha()):#Verifico se o contato é entre 8 e 15
                        break # Se passou ele vai para o próximo campo

                    else:
                        tentativas_contatos += 1
                        print(f"Informe apenas caracteres do tipo inteiro --- Tentativa {tentativas_contatos} de 3") 
                        
                    if tentativas_contatos == 3:
                        print("QTD de vezes atigingida")
                        exit()

            while tentativas_contatos < 3:# while interno para contar o número de tentativas

                email_contato = input("E-mail:")
                if("@" in email_contato and ".com" in email_contato):## Vejo se @ e .com estão no texto que o usuário digitou
                    break 

                else:
                    print("E-mail Inválido")   
                    print(f" Tentativa {tentativas_contatos} de 3") 

                if tentativas_contatos == 3:
                    print("QTD de vezes atigingida")
                    exit()
      
            contatos.append(f'{nome_contato}|{telefone_contato}|{email_contato}')
            # Método append para adicionar os contatos na última posição da lista
            qtd_de_contatos_cadastrados += 1# Contabiliza um contato cadastrado
            print("-----------------------------------------")
            print(f"Contatos Cadastrados = {qtd_de_contatos_cadastrados}") # Mostra a qtd de contatos cadastrados


            if qtd_de_contatos_cadastrados == total_contatos:
                # Se cadastrar todos os contatos, ele sai e exibi os contatos cadastrados
                print("-----------------------------------------")
                print("Você já atingiu o limite máximo de contatos:")
                print("Contatos cadastrados:")
                for contato in contatos:
                    print(contato)
                print("-----------------------------------------")
                exit()

            sair_sistema = input("Deseja sair do sistema? (Sim|Não)").strip().upper()
            # Se deseja sair do sistema, ele sai e imprime os contatos
            if(sair_sistema == "SIM"):
                print("-----------------------------------------")
                print("Contatos cadastrados:")
                for contato in contatos:
                    print(contato)
                print("Saindo....")
                time.sleep(0.80)
                exit()

            vizualizar_contatos = input("Deseja visualizar seus contatos? (Sim|Não): ").strip().upper()
            # Se vizualizar, ele mostra os contatos
            if vizualizar_contatos == "SIM":
                print("Contatos cadastrados:")
                print("-----------------------------------------")
                for contato in contatos:
                    print(contato)   
                print("-----------------------------------------")
             
    
            if qtd_de_contatos_cadastrados < total_contatos:
                cadastrar_novo_contato = input("Deseja cadastrar outro contato? (Sim|Não): ").strip().upper()
                if cadastrar_novo_contato != "SIM":
                    print("Saindo.....")
                    time.sleep(0.80)
                    break

            


  



                
      
  



