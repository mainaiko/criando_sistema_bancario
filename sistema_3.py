from abc import ABC, abstractclassmethod, abstractproperty

class Cliente:
     def __init__(self, endereco):
          self.endereco = endereco
          self.conta = []
    
     def realizar_transacao(self, conta, transacao):
          transacao.registrar(conta)
    
     def adicionar_conta(self, conta):
        self.conta.append(conta)

class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf      

class Conta:
     def __init__(self, numero, cliente):    
        self._saldo = 0
        self._numero = numero
        self._agencia = "001"
        self._cliente = cliente
        self._hitorico = Historico() 

     @classmethod
     def nova_conta(cls, cliente, numero):
         return cls(numero, cliente) 
     
     @property
     def saldo(self):
         return self._saldo
     
     @property
     def numero(self):
         return self._numero
     
     @property
     def agencia(self):
         return self._agencia
    
     @property
     def cliente(self):
         return self._cliente

     @property
     def historico(self):
         return self._historico
     
     @property
     def sacar(self, valor):
         saldo = self._saldo
         excedeu_saldo = valor > saldo

         if excedeu_saldo:
            print("\n Operaçao falhou! Você nao tem saldo suficiente.")
         elif valor > 0:
            self._saldo -= valor
            print ("\n Saque relizado com sucesso!")
            return True
         else:
            print ("\n Operação falhou, valor informado invalido")
            return False
     @property
     def depositor(self, valor):
         if valor > 0:
            self._saldo += valor
            print("\nDeposito realizado com sucesso!")
            return True
         else:
            print("Operaçao falhou, valor informado invalido")
            return False

class Conta_Corrente (Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saque =limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__
            ]
        )
        excedeu_limite = valor > self.saldo
        excedeu_saques = numero_saques >= self.limite_saque

        if excedeu_limite:
            print("\n Operaçao falhou! Você nao tem limite suficiente.")
        elif excedeu_saques:
            print("\n Operaçao falhou! Você nao tem saques suficiente.")
        else:
            return super().sacar(valor)
        
        return False
        
    def __str__(self):
        return f"""
    Agencia: {self.agencia}
    C/C: {self.numero}
    Titular {self.cliente.nome}
    """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)