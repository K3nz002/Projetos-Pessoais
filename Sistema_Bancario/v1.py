from datetime import datetime

saldo = 0
extrato_historico = []
saques_diarios = 0
ultimo_saque_diario = None

def deposito():
    global saldo, extrato_historico
    deposito = float(input('Digite o valor que deseja depositar: '))
    horario_atual = datetime.now()

    if deposito > 0:
        historico = f'Depósito: R$ {deposito} | {horario_atual.hour}:{horario_atual.minute}:{horario_atual.second} | {horario_atual.day}/{horario_atual.month}/{horario_atual.year}'
        print(historico)
        extrato_historico.append(historico)
        saldo += deposito
        print('Depósito realizado com sucesso')
        return deposito

    else:
        print('O valor informado é inválido.')
        return deposito

def saque():
    global saques_diarios, saldo, extrato_historico, ultimo_saque_diario
    horario_atual = datetime.now()

    # Verifica se o dia mudou para resetar a contagem de saques diários
    if ultimo_saque_diario != horario_atual.day:
        saques_diarios = 0
        ultimo_saque_diario = horario_atual.day

    if saques_diarios >= 3:
        print('Limite diário de 3 saques atingido. Tente novamente amanhã.')
        return saque

    saque = float(input('Digite o valor que deseja sacar: '))

    if saque > 0 and saque <= 500 and saque <= saldo:
        historico = f'Saque: R$ {saque} | {horario_atual.hour}:{horario_atual.minute}:{horario_atual.second} | {horario_atual.day}/{horario_atual.month}/{horario_atual.year}'
        saldo -= saque
        print(historico)
        extrato_historico.append(historico)
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