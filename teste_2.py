import textwrap

class main():

    def menu(self):
        menu = """\n
        [a]\tDeposito
        [b]\tSaque
        [c]\tExtrato
        [s]\tNova conta 
        [f]\tListar contas
        [g]\tNovo usuario
        [d]\tSair
        """
        return input((menu))
    
    def pagina(self):
        LIMITE_SAQUES = 3
        AGENCIA = "0001"

        saldo = 0
        saque_maximo= 500
        extrato = []
        numero_de_saques = 0
        usuarios = []
        contas = []
        limite = 500

        while True:
            opcao = self.menu()

            if opcao == "a":
                valor = float(input ("Informe o valor do deposito: "))
                saldo, extrato = self.depositar(saldo,valor,extrato)
            elif opcao == "b":
                valor = float(input("Informe o valor do saque: "))
                saldo,extrato = self.sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_de_saques=numero_de_saques,
                    limite_saques=LIMITE_SAQUES,
                )
            elif opcao == "c":
                self.exibir_extrato(saldo, extrato= extrato)
            elif opcao == "g":
                self.criar_usuario(usuarios)
            elif opcao == "s":
                numero_conta = len(contas) + 1
                conta = self.criar_conta(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            elif opcao == "f":
                self.listar_contas(contas)
            elif opcao == "d":
                break
            else:
                print("Operaçao invalida, tente novamente")

    def depositar(self, saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            print("\nDeposito realizado com sucesso!")
        else:
            print("Operaçao falhou, valor informado invalido")
        return saldo, extrato
    
    def sacar(self, *, saldo, valor, extrato, limite, numero_de_saques, limite_saques):
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
            extrato += f"Saque:\tR$ {valor:.2f}\n"
            numero_de_saques += 1
            print ("\n Saque relizado com sucesso!")
        else:
            print ("\n Operação falhou, valor informado invalido")
        return saldo, extrato

    def exibir_extrato (self, saldo, / , extrato):
        print ("\n=====================EXTRATO=====================")
        print ("Nao foram realizadas movimentaçoes." if not extrato else extrato)
        print (f"\nSaldo R$ {saldo:.2f}")
        print ("================================================")

    def criar_usuario(self, usuarios):
        cpf = input("Informe o CPF(somente numeros): ")
        usuario = self.filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\n Ja existe um usuario com este CPF")
            return
        nome = input("Informe seu nome completo: ")
        data_nascimento = input("informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nmr, bairro, cidade, estado): ")

        usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print ("Usuario criado com sucesso!")

    def filtrar_usuario(self, cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None
    
    def criar_conta(self, agencia, numero_conta, usuarios):
        cpf= input("Iforme o CPF do usuario: ")
        usuario= self.filtrar_usuario(cpf, usuarios)

        if usuario:
            print("\nConta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        print("\n Usuario nao encontrado, criaçao de conta encerrado!")

    def listar_contas(self, contas):
        for conta in contas:
            linha = f"""\
                Agencia:\t{conta["agencia"]}
                C/C:\t\t{conta["numero_conta"]}
                Titular:\t{conta["usuario"]["nome"]}
            """
            print ("="*100)
            print (textwrap.dedent(linha))
    
conta_1 = main().pagina()
print (conta_1)