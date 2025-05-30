from datetime import datetime, timedelta

# Váriaveis globais // globals variables

saldo = 0
extrato_historico = []
saques_diarios = 0
ultimo_saque_diario = None
transacoes_diarias = 0
ultima_transacao = None
agencia = '0001'
usuarios = {}
conta = {}

def main(): # menu principal // main menu
    while True:
        opcao = int(input('''Escolha a operação desejada:

        [1] Deposito
        [2] Saque
        [3] Extrato
        [4] Criar usuário
        [5] Criar conta
        [0] Sair

        => '''))

        if opcao == 1:
            print('Depósito')
            deposito()
        elif opcao == 2:
            print('Saque')
            saque()
        elif opcao == 3:
            print('Extrato')
            extrato()
        elif opcao == 4:
            print('Criar usuário')
            criar_usuario()
        elif opcao == 5:
            print('Criar conta')
            criar_conta()
        elif opcao == 0:
            break
        else:
            print('Operação inválida, selecione novamente a operação desejada.')

def criar_usuario(): # cadastro de usuário // user registration
    global usuarios
    nome = input('Digite seu nome:\n')
    cpf = int(input('Digite o CPF(somente números):\n'))

    if cpf < 11:
        print('CPF inválido.')
        return criar_usuario()

    data_nascimento = input('Digite a sua data de nascimento seguindo o seguinte formato\ndd/mm/aaaa:\n')

    if data_nascimento < 8:
        print('Data de nascimento inválida.')
        return criar_usuario()

    endereco = input('Digite o endereço seguinto o seguinte formato\nlogradouro, n° - bairro - cidade/sigla do estado:\n')

    if cpf in usuarios:
        print('Usuário já cadastrado.')
        return criar_usuario()
    else:
        usuarios.update({cpf: {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco}})
        print('Usuário cadastrado com sucesso.')
        return usuarios

def criar_conta(): # criação de conta // account creation
    global agencia, usuarios
    # nr_conta = len(conta) + 1 # propricio a erros se tivesse que excluir contas
    nr_conta = 1
    cpf = int(input('Digite o CPF do usuário:\n'))

    if cpf in usuarios:
        conta.update({nr_conta:{'agencia': agencia, 'cpf': cpf}})
        print('Conta criada com sucesso.')
        nr_conta += 1
        print(conta)
    else:
        print('Usuário não cadastrado.')
        return criar_usuario()

def deposito(): # depósito // deposit
    global saldo, extrato_historico, transacoes_diarias, ultima_transacao
    deposito = float(input('Digite o valor que deseja depositar:\n'))
    horario_atual = datetime.now()

    if ultima_transacao != horario_atual.day:
        transacoes_diarias = 0
        ultima_transacao = horario_atual.day

    if transacoes_diarias >= 10 and ultima_transacao == horario_atual.day:
        print('Limite diário de 5 transações atingido. Tente novamente amanhã.')
        return deposito

    if deposito > 0:
        historico = f'Depósito: R$ {deposito} | {horario_atual.hour}:{horario_atual.minute}:{horario_atual.second} | {horario_atual.day}/{horario_atual.month}/{horario_atual.year}'
        print(historico)
        extrato_historico.append(historico)
        saldo += deposito
        transacoes_diarias += 1  # Incrementa a contagem de transações diárias após o depósito em vez de antes
        print('Depósito realizado com sucesso')
        return deposito

    else:
        print('O valor informado é inválido.')
        return deposito

def saque(): # saque // withdraw
    global saques_diarios, saldo, extrato_historico, ultimo_saque_diario, transacoes_diarias, ultima_transacao
    horario_atual = datetime.now()

    if ultima_transacao != horario_atual.day:
        transacoes_diarias = 0
        ultima_transacao = horario_atual.day

    if transacoes_diarias >= 10 and ultima_transacao == horario_atual.day:
        print('Limite diário de 5 transações atingido. Tente novamente amanhã.')
        return deposito
    
    # Verifica se o dia mudou para resetar a contagem de saques diários
    if ultimo_saque_diario != horario_atual.day:
        saques_diarios = 0
        ultimo_saque_diario = horario_atual.day

    if saques_diarios >= 3 and ultimo_saque_diario == horario_atual.day:
        print('Limite diário de 3 saques atingido. Tente novamente amanhã.')
        return saque

    saque = float(input('Digite o valor que deseja sacar:\n'))

    if saque > 0 and saque <= 500 and saque <= saldo:
        historico = f'Saque: R$ {saque} | {horario_atual.hour}:{horario_atual.minute}:{horario_atual.second} | {horario_atual.day}/{horario_atual.month}/{horario_atual.year}'
        saldo -= saque
        print(historico)
        extrato_historico.append(historico)
        transacoes_diarias += 1  # Incrementa a contagem de transações diárias após o saque em vez de antes
        saques_diarios += 1
        print('Saque realizado com sucesso.')
        return saque

    elif saque > saldo:
        print('Saldo insuficiente para saque.')
        return saque

    else:
        print('Valor de saque inválido.')
        return saque

def extrato(): # extrato // statement
    global saldo, extrato_historico
    print('Extrato')
    if extrato_historico:
        for operacao in extrato_historico:
            print(operacao)

    else:
        print('Nenhuma transação registrada.')
    print(f'Saldo atual: R$ {saldo}')

main()