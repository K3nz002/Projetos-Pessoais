import string

def verificar_senha(senha):
    # Verifica se a senha é válida
    senha_invalidas = ['12345678', 'password', 'senha123', 'qwerty123']
    comprimento_minimo = len(senha) >= 8
    comprimento_seguro = len(senha) >= 16
    caracter_maiusculo = any (char in string.ascii_uppercase for char in senha)
    caracter_numero = any (char in string.digits for char in senha)
    caracter_pontuacao = any (char in string.punctuation for char in senha)

    # Calcula o percentual de segurança da senha
    pontuacao = sum([comprimento_minimo, comprimento_seguro,
    caracter_pontuacao, caracter_numero, caracter_maiusculo])

    if senha in senha_invalidas:
        print('Senha inválida, percentual de segurança: 0%')
    elif len(senha) < 8:
        print('Senha muito curta, percentual de segurança: 0%')

    dicas_senhas = print('Aqui está algumas dicas para melhorar sua senha:\n- Não use palavras comuns como senha.\n- Escreva uma senha com letras maiúsculas e minúsculas.\n- Use caracteres especiais como !@#$%^&*()_+\n- Não use informações pessoais como senha.\n- Use uma senha com pelo menos 16 caracteres.\n- Use números na sua senha.')
    match pontuacao:
        case 1:
            print('Senha muito fraca, percentual de segurança: 20%')
            print(dicas_senhas)
        case 2:
            print('Senha fraca, percentual de segurança: 40%')
            print(dicas_senhas)
        case 3:
            print('Senha média, percentual de segurança: 60%')
            print(dicas_senhas)
        case 4:
            print('Senha forte, percentual de segurança: 80%')
            print(dicas_senhas)
        case 5:
            print('Senha muito forte, percentual de segurança: 100%')
    
senha = input('Digite a senha que você gostaria de verificar: ')
verificar_senha(senha)
