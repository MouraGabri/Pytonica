import time

def boas_vindas():
    print("|----------------------------------------------------------------------------------|")
    print("|                                                                                  |")
    print("|                         Seja bem vindo a Pythônica!!                             |")
    print("|                                                                                  |")
    print("|                                                                                  |")
    print("|----------------------------------------------------------------------------------|")

qtd_min_caracteres = int(3)## qtd minima de caracteres para o nome
tentativas_nome = 1
nome = False

def validacao_nome():
    global nome
    global tentativas_nome
    global nome_usuario

    print("Para seguir na plataforma, informe o seu nome.")
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

def menu_opcoes():
    global cadastrar_contatos
    global tentativas_opcoes
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


def cadastrar_nome():
    tentativas_contato = 0
    global nome_contato
    while tentativas_contato < 3:
        nome_contato = input("Nome:").strip()

        if len(nome_contato)> qtd_min_caracteres and nome_contato.replace(" ", "").isalpha(): ##isalpha(verifica se todos os caracteres são letras)
            print("Passou na validação do nome")
            break
        else:
            tentativas_contato += 1   
            print(f"Informe apenas caracteres do tipo texto --- Tentativa {tentativas_contato} de 3") 

        if   tentativas_contato == 3:
            print("QTD de vezes atigingida")
            exit()  


def cadastrar_telefone():
    telefone_tentativa = 0
    global telefone
    while telefone_tentativa < 3:# while interno para contar o número de tentativas
        telefone = input("Telefone:").strip()## Cada interação ele pede um novo telefone

        if(len(telefone) > 8 and len(telefone) < 15  and  not telefone.isalpha()):#Verifico se o contato é entre 8 e 15
            print("Passou na validação do nome")
            break # Se passou ele vai para o próximo campo

        else:
            telefone_tentativa += 1
            print(f"Informe apenas caracteres do tipo inteiro --- Tentativa {telefone_tentativa} de 3") 
                        
        if telefone_tentativa == 3:
            print("QTD de vezes atigingida")
            exit()

def cadastrar_email():
    tentativa_email = 0
    global email_contato
    while tentativa_email < 3:
        email_contato = input("E-mail:")
        if("@" in email_contato and ".com" in email_contato):## Vejo se @ e .com estão no texto que o usuário digitou
            print("Passou na validação do email")
            break 

        else:            
            tentativa_email += 1
            print(f"E-mail Inválido | Tentativa {tentativa_email} de 3 ")   

        if tentativa_email == 3:
            print("QTD de vezes atigingida")
            exit()
        
def lista_contatos_cadastrados():
    lista_contatos = []
    lista_contatos.append(f'{nome_contato} | {telefone} | {email_contato}')
    for i in lista_contatos:
        print(i)

def salvar_csv():
    import pandas as pd


    df = pd.DataFrame({
        "Nome": nome_contato,
        "Telefone": telefone,
        "E-Mail": email_contato
    },index=[0])

    df.to_excel("Faculdade_G2.xlsx", header=True, index=False, engine='openpyxl')

def main():
   boas_vindas()
   validacao_nome()
   menu_opcoes()
   cadastrar_nome()
   cadastrar_telefone()
   cadastrar_email()
   salvar_csv()
main()   
