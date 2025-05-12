import requests

def cotacao_moedas():
    # API das cotações de moedas estrangeiras e bitcoin
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,JPY-BRL,CNY-BRL')
    lista_cotacoes = cotacoes.json()
    cotacao_dolar = float(lista_cotacoes['USDBRL']['bid'])
    cotacao_euro = float(lista_cotacoes['EURBRL']['bid'])
    cotacao_iene = float(lista_cotacoes['JPYBRL']['bid'])
    cotacao_yuan = float(lista_cotacoes['CNYBRL']['bid'])

    print('Escolha uma moeda:\n1. Dólar\n2. Euro\n3. Iene Japonês\n4. Yuan Chinês')
    moeda = int(input())

    match moeda:

        case 1:
            print('Escolha a operação que gostaria de fazer\n1. USD -> Real\n2. Real -> USD')
            operacao = int(input())

            match operacao:

                case 1:
                    while True:
                        valor_dolar = float(input('Digite o valor em dólar: '))
                        print(f'O valor de dólar para real é R${valor_dolar * cotacao_dolar: .2f}')
                        if valor_dolar == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para dólar é ${valor_real / cotacao_dolar: .2f}')
                        if valor_real == 0:
                            break

        case 2:
            print('Escolha a operação que gostaria de fazer\n1. EUR -> Real\n2. Real -> EUR')
            operacao = int(input())

            match operacao:

                case 1:
                    while True:
                        valor_euro = float(input('Digite o valor em euro: '))
                        print(f'O valor de euro para real é R${valor_euro * cotacao_euro: .2f}')
                        if valor_euro == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para euro é €{valor_real / cotacao_euro: .2f}')
                        if valor_real == 0:
                            break

        case 3:
            print('Escolha a operação que gostaria de fazer\n1. JPY -> Real\n2. Real -> JPY')
            operacao = int(input())
            
            match operacao:

                case 1:
                    while True:
                        valor_iene = float(input('Digite o valor em Iene: '))
                        print(f'O valor de Iene para real é R${valor_iene * cotacao_iene: .2f}')
                        if valor_iene == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para Iene é ¥{valor_real / cotacao_iene: .2f}')
                        if valor_real == 0:
                            break

        case 4:
            print('Escolha a operação que gostaria de fazer\n1. CNY -> Real\n2. Real -> CNY')
            
            operacao = int(input())

            match operacao:

                case 1:
                    while True:
                        valor_cny = float(input('Digite o valor em yuan chinês: '))
                        print(f'O valor de yuan chinês para real é R${valor_cny * cotacao_yuan: .2f}')
                        if valor_cnh == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para yuan chinês é ¥{valor_real / cotacao_yuan: .2f}')
                        if valor_real == 0:
                            break

        case _:
            print('Escolha inválida')

# Execução do programa
cotacao_moedas()