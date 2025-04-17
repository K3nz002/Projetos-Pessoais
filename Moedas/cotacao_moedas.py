import requests

def cotacao_moedas():
    # API das cotações de moedas estrangeiras e bitcoin
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    lista_cotacoes = cotacoes.json()
    cotacao_dolar = float(lista_cotacoes['USDBRL']['bid'])
    cotacao_euro = float(lista_cotacoes['EURBRL']['bid'])
    cotacao_btc = float(lista_cotacoes['BTCBRL']['bid'])

    print('Escolha uma moeda:\n1. Dólar\n2. Euro\n3. Bitcoin')
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
                        print(f'O valor de real para euro é €{valor_real / cotacao_euro:.2f}')
                        if valor_real == 0:
                            break

        case 3:
            print('Escolha a operação que gostaria de fazer\n1. BTC -> Real\n2. Real -> BTC')
            operacao = int(input())
            match operacao:

                case 1:
                    while True:
                        valor_btc = float(input('Digite o valor em bitcoin: '))
                        print(f'O valor de bitcoin para real é R${valor_btc * cotacao_btc}')
                        if valor_btc == 0:
                            break

                case 2:
                    while True:
                        valor_real = float(input('Digite o valor em real: '))
                        print(f'O valor de real para bitcoin é ₿{valor_real / cotacao_btc}')
                        if valor_real == 0:
                            break

def grafico_variacao(moeda):
    pass