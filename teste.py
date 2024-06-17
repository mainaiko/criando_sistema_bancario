# testes para aula 2

def usuario(*, nome, idade, cpf, data_nascimento):
    print (f"nome= aiko, idade= 21")
    
usuario()
def deposito_def():
    global saldo
    if deposito > 0:
        saldo += deposito
        extrato.append (f"Deposito de {deposito}")
    else:
        print("Operaçao falhou ou valor informado invalido")

def saque_def():
    global saldo
    global saque
    global saque_maximo
    global numero_de_saques
    global LIMITE_DE_SAQUES
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > saque_maximo
    excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES


    while True:
        if saque:
            saldo -= saque
            extrato.append (f"Saque de {saque}")
            numero_de_saques += 1
            if not excedeu_saques:
                    print (f"Saque de: {saque}, realizado com sucesso")
        break
            

        if excedeu_saldo:
            print ("Operaçao falhou! Voce nao tem saldo suficiente")
        elif excedeu_limite:
            print ("Operaçao falhou! Voce nao tem limite suficiente")
        elif excedeu_saques:
            print ("Operaçao falhou! Voce nao tem saques disponiveis")
        else:
            pass

def extrato_def():
    print ("\n=====================EXTRATO=====================")
    print ("Nao foram realizadas movimentaçoes." if not extrato else extrato)
    print (f"\nSaldo R$ {saldo:.2f}")
    print ("================================================")

def usuario(*, nome, idade, cpf, data_nascimento):
    print(f"Usuario criado com sucesso:\n{nome}\n{idade}\n{cpf}\n{data_nascimento}")

def criar_conta_corrente(*, agencia, numero_da_conta, usuario):
    print(f"Conta criada com sucesso:\n{agencia}\n{numero_da_conta}\n{usuario()}")




escolha_1 = input("Deseja criar um usuario?\n").lower()
if escolha_1 == "sim":
    usuario(nome= (input("Qual seu nome: ")), idade= (input("Qual sua idade: ")), cpf= (input("Qual seu cpf: ")), data_nascimento= (input("Qual sua data de nascimento: ")))
else:
    print("Obrigado por usar nossos serviços")

escolha_2 = input("Deseja cirar sua conta corente?\n").lower()
if escolha_1 == "sim":
    usuario(agencia= "0001", numero_da_conta= ("1"+{random(100000,900000)}), cpf= (input("Qual seu cpf: ")), data_nascimento= (input("Qual sua data de nascimento: ")))
else:
    print("Obrigado por usar nossos serviços")



while True:

    opcao_escolhida = input(main).lower()
    if opcao_escolhida == "a":
        deposito = float(input("Valor a depositar: "))
        deposito_def()
    elif opcao_escolhida == "b":
        saque = float(input("Valor a sacar: "))
        saque_def()
    elif opcao_escolhida == "c":
        extrato_def()
    elif opcao_escolhida == "d":
        break
    else:
        print("Operaçao invalida, por favor selecione uma opção")

