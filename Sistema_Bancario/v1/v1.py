from datetime import datetime, timedelta

saldo = 0
extrato_historico = []
saques_diarios = 0
ultimo_saque_diario = None
transacoes_diarias = 0
ultima_transacao = None

def deposito():
    global saldo, extrato_historico, transacoes_diarias, ultima_transacao
    deposito = float(input('Digite o valor que deseja depositar: '))
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

def saque():
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

    saque = float(input('Digite o valor que deseja sacar: '))

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

def extrato():
    if extrato_historico:
        for operacao in extrato_historico:
            print(operacao)

    else:
        print('Nenhuma transação registrada.')
    print(f'Saldo atual: R$ {saldo}')

while True:
    opcao = int(input('''Escolha a operação desejada:

    [1] Deposito
    [2] Saque
    [3] Extrato
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
    elif opcao == 0:
        break
    else:
        print('Operação inválida, selecione novamente a operação desejada.')