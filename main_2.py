# criado na aula

import textwrap

def menu():
    menu = """\n
    [a]\tDeposito
    [b]\tSaque
    [c]\tExtrato
    [s]\tNova conta 
    [f]\tListar contas
    [g]\tNovo usuario
    [d]\tSair
    """
    return input(textwrap.dedent(menu))

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"


    saldo = 0
    saque_maximo= 500
    extrato = []
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "a":
            valor = float(input ("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo,valor,extrato)
        elif opcao == "b":
            valor = float(input("Informe o valor do saque"))
            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                limite_saques=LIMITE_DE_SAQUES,
            )
        elif opcao == "c":
            exibir_extrato(saldo, extrato= extrato)
        elif opcao == "g":
            criar_usuario(usuarios)
        elif opcao == "s":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "f":
            listar_contas(contas)
        elif opcao == "d":
            break
        else:
            print("Operaçao invalida, tente novamente")
        
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"deposito:\tR$ {valor:.2f}\n"
        print("\nDeposito realizado com sucesso!")
    else:
        print("Operaçao falhou, valor informado invalido")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques >= limite_saques

    if excedeu_saldo:
        print("\n Operaçao falhou! Você nao tem saldo suficiente.")
    elif excedeu_limite:
        print("\n Operaçao falhou! Você nao tem limite suficiente.")
    elif excedeu_saques:
        print("\n Operaçao falhou! Você nao tem saques suficiente.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_de_saques += 1
        print ("\n Saque relizado com sucesso!")
    else:
        print ("\n Operação falhou, valor informado invalido")
    return saldo, extrato

def exibir_extrato (saldo, / , extrato):
    print ("\n=====================EXTRATO=====================")
    print ("Nao foram realizadas movimentaçoes." if not extrato else extrato)
    print (f"\nSaldo R$ {saldo:.2f}")
    print ("================================================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Ja existe um usuario com este CPF")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nmr, bairro, cidade, estado): ")

    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print ("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf= input("Iforme o CPF do usuario: ")
    usuario= filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n Usuario nao encontrado, criaçao de conta encerrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print ("="*100)
        print (textwrap.dedent(linha))
  

main()