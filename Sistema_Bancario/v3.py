from abc import ABC, abstractmethod
from datetime import datetime

class Conta:
    def __init__ (self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
  
    @classmethod
    def nova_conta(cls, numero, cliente):
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

    def sacar(self, valor):
        if self._saldo < valor:
            print('Saldo insuficiente para saque.')

        elif valor > 0:
            self._saldo -= valor
            print('Saque realizado com sucesso.')
            return True

        else:
            print('Valor inválido para saque.')
            
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito realizado com sucesso.')
            return True

        else:
            print('Valor inválido para depósito.')
        
        return False
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite, limite_saques_diarios, limite_transacao_diaria):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques_diarios = limite_saques_diarios
        self._limite_transacao_diaria = limite_transacao_diaria

    def verificador_transacoes_diarias(self):
        hoje = datetime.now().strftime("%d-%m-%Y")
        num_transacoes = len(
            [transacao for transacao in self.historico.transacoes 
             if transacao["Data"].startswith(hoje)]
        )

        if num_transacoes >= self._limite_transacao_diaria:
            print(f'Limite de {self._limite_transacao_diaria} transações diárias excedido.')
            return False
        
        return True

    def sacar(self, valor):
        if not self.verificador_transacoes_diarias():
            return False
            
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["Tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print('Valor de saque excede o limite.')

        elif numero_saques >= self._limite_saques_diarios:
            print(f'Limite de {self._limite_saques_diarios} saques diários excedido.')

        else:
            return super().sacar(valor)
        
        return False
    
    def depositar(self, valor):
        if not self.verificador_transacoes_diarias():
            return False
            
        return super().depositar(valor)
    
    def __str__(self):
        return f"Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente.nome}"

class Cliente:
    def __init__ (self, endereco):
        self._endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class Historico:
    def __init__ (self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        hora_atual = datetime.now()
        self._transacoes.append(
            {
                'Tipo': transacao.__class__.__name__,
                'Valor': transacao.valor,
                'Data': hora_atual.strftime('%d-%m-%Y | %H:%M:%S')
            }
        )

class PessoaFisica(Cliente):
    def __init__ (self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
    
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__ (self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar (self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__ (self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar (self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

def main():
    contas = [] 
    clientes = []

    while True:
        opcao = int(input('''Escolha a operação desejada:

        [1] Deposito
        [2] Saque
        [3] Extrato
        [4] Criar usuário
        [5] Criar conta
        [6] Listar contas
        [0] Sair

        => '''))

        if opcao == 1:
            print('Depósito')
            deposito(clientes)

        elif opcao == 2:
            print('Saque')
            saque(clientes)

        elif opcao == 3:
            print('Extrato')
            extrato(clientes)

        elif opcao == 4:
            print('Criar usuário')
            criar_usuario(clientes)

        elif opcao == 5:
            print('Criar conta')
            numero = len(contas) + 1
            criar_conta(numero, clientes, contas)

        elif opcao == 6:
            print('Listar contas')
            listar_contas(contas)

        elif opcao == 0:
            break
        else:
            print('Operação inválida, selecione novamente a operação desejada.')

def deposito(clientes):
    cpf = input('Informe o CPF do cliente:\n')
    if len(cpf)!= 11:
        print('CPF inválido!')
        return deposito(clientes)

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return criar_usuario(clientes)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print('Conta não encontrada!')
        return criar_conta(numero, clientes, contas)

    valor = float(input('Digite o valor que deseja depositar:\n'))
    transacao = Deposito(valor)

    cliente.realizar_transacao(conta, transacao)

def saque(clientes):
    cpf = input('Informe o CPF do cliente:\n')
    if len(cpf)!= 11:
        print('CPF inválido!')
        return saque(clientes)

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return criar_usuario(clientes)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print('Conta não encontrada!')
        return criar_conta(numero, clientes, contas)

    valor = float(input('Digite o valor que deseja sacar:\n'))
    transacao = Saque(valor)

    cliente.realizar_transacao(conta, transacao)

def extrato(clientes):
    cpf = input('Informe o CPF do cliente:\n')
    if len(cpf)!= 11:
        print('CPF inválido!')
        return extrato(clientes)

    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return criar_usuario(clientes)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print('Conta não encontrada!')
        return criar_conta(numero, clientes, contas)

    print('Extrato')
    transacoes = conta.historico.transacoes

    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transacoes:
            extrato += f'{transacao["Tipo"]}:\n\tR$ {transacao["Valor"]:.2f} | {transacao["Data"]}'
    print(extrato)
    print(f'\nSaldo:\n\tR$ {conta.saldo:.2f}')

def criar_usuario(clientes):
    cpf = input('Informe o CPF para criar o seu usuário (somente número):\n')
    if len(cpf) != 11:
        print('CPF inválido!')
        return criar_usuario(clientes)
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print('Já existe cliente com esse CPF!')
        return criar_usuario(clientes)

    nome = input('Informe o nome completo:\n')
    data_nascimento = input('Informe a data de nascimento seguindo o modelo: (dd-mm-aaaa)\n')
    if len(data_nascimento)!= 10:
        print('Data de nascimento inválida!')
        return criar_usuario(clientes)

    endereco = input('Informe o endereço (logradouro, nro - bairro - cidade/sigla estado):\n')

    cliente = PessoaFisica(
        endereco = endereco,
        cpf = cpf,  
        nome = nome,
        data_nascimento = data_nascimento
    )
    clientes.append(cliente)

    print('Usuário criado com sucesso!')

def criar_conta(numero, clientes, contas):
    cpf = input('Informe o CPF do cliente:\n')
    if len(cpf)!= 11:
        print('CPF inválido!')
        return criar_conta(numero, clientes, contas)
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado!')
        return criar_usuario(clientes)

    limite = int(input('Informe o valor de saque limite da conta:\n'))
    limite_saques_diarios = int(input('Informe o limite de saques diários:\n'))
    limite_transacao_diaria = int(input('Informe o limite de transação diária:\n'))


    if not cliente:
        print('Cliente não encontrado!')
        return criar_usuario(clientes)

    conta = ContaCorrente(
        numero = numero,
        cliente = cliente,
        limite = limite,
        limite_saques_diarios = limite_saques_diarios,
        limite_transacao_diaria = limite_transacao_diaria
    )

    contas.append(conta)
    cliente.contas.append(conta)
    
    print('Conta criada com sucesso!')
    print(str(conta))

def listar_contas(contas):
    for conta in contas:
        print(str(conta))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente): 
    if not cliente.contas:
        print('Cliente não possui conta!')
        return main()

    else:
        num_conta = int(input('Informe o número da conta:\n')) - 1
        return cliente.contas[num_conta]
 
main()
    
        

