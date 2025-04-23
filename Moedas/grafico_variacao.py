import plotly.graph_objects as go
import pandas as pd
import requests

def grafico_variacao():
    
    # Montagem da URL para a API de cotações
    moeda_base = int(input('Escolha a moeda base: \n1. Dólar\n2. Euro\n3. Iene Japonês\n4. Yuan Chinês\n'))
    moeda_referencia = int(input('Escolha a moeda de referência: \n1. Real\n2. Dólar\n3. Euro\n4. Iene Japonês\n5. Yuan Chinês\n'))
        
    match moeda_base:
        case 1:
            moeda_base = 'USD'
        case 2:
            moeda_base = 'EUR'
        case 3:
            moeda_base = 'JPY'
        case 4:
            moeda_base = 'CNY'
        case _:
            print('Escolha inválida')
            return

    match moeda_referencia:
        case 1:
            moeda_referencia = 'BRL'
        case 2:
            moeda_referencia = 'USD'
        case 3:
            moeda_referencia = 'EUR'
        case 4:
            moeda_referencia = 'JPY'
        case 5:
            moeda_referencia = 'CNY'
        case _:
            print('Escolha inválida')
            return

    ano_inicial = int(input('Digite o ano inicial a partir do ano 2008: '))
    if ano_inicial < 2008:
        print('Ano inválido')
        return

    ano_final = int(input('Digite o ano final: '))
    if ano_final < ano_inicial:
        print('Ano inválido')
        return

    data_inicial = f'{ano_inicial}-01-01'
    data_final = f'{ano_final}-12-31'

    conversao_api = requests.get(f'https://api.frankfurter.dev/v1/{data_inicial}..{data_final}?base={moeda_base}&symbols={moeda_referencia}')
    dict_variacao = conversao_api.json()
    
    # Tratamento dos dados para datas e cotações
    datas = list(dict_variacao['rates'].keys())
    valores_variacao = [dict_variacao['rates'][data]['BRL'] for data in datas]

    # Criação do gráfico de linha com Plotly
    sifrao_moedas = {
        'USD': '$',
        'EUR': '€',
        'JPY': '¥',
        'CNY': '¥',
        'BRL': 'R$'
    }

    txt_moedas = {
        'USD': 'Dólar',
        'EUR': 'Euro',
        'JPY': 'Iene Japonês',
        'CNY': 'Yuan Chinês',
        'BRL': 'Real'
    }

    fig = go.Figure(go.Scatter(x = datas, y = valores_variacao, mode = 'lines'))
    fig.update_layout(
        title = f'Variação da cotação do {txt_moedas[moeda_base]} em relação ao {txt_moedas[moeda_referencia]}', xaxis_title = 'Data', yaxis_title = 'Cotação', 
        yaxis_tickprefix = sifrao_moedas[moeda_referencia], yaxis_tickformat = '.2f', xaxis_tickformat = ('%Y-%m-%d'),
        )
    fig.show()

# Execução do programa
grafico_variacao()