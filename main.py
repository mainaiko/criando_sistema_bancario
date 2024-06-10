main = """
[a]Deposito
[b]Saque
[c]Extrato
[d]Sair
"""

saldo = 0
saque_maximo= 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao_escolhida = input(main)

    if opcao_escolhida == "a":
        deposito = float(input("Valor a depositar: "))
        if deposito > 0:
            saldo == deposito
            extrato == f"Deposito: R${deposito:.2f}\n"
        else:
            print("Operaçao falhou ou valor informado invalido")
    elif opcao_escolhida == "b":
        saque = float(input ("Valor a sacar: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > saque_maximo
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES


        if excedeu_saldo:
            print ("Operaçao falhou! Voce nao tem saldo suficiente")
        elif excedeu_limite:
            print ("Operaçao falhou! Voce nao tem limite suficiente")
        elif excedeu_saques:
            print ("Operaçao falhou! Voce nao tem saques disponiveis")
        else:
            print ("Valor informado invalido")
    elif opcao_escolhida == "c":
        print ("\n=====================EXTRATO=====================")
        print ("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print (f"\nSaldo R$ {saldo:.2f}")
        print ("================================================")

    elif opcao_escolhida == "d":
        break
    else:
        print("Operaçao invalida, por favor selecione uma opão")


