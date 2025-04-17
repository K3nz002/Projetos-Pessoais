import random
import string

def senha_fraca(comprimento):
    caracteres = string.ascii_letters
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_medio(comprimento):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_forte(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

nivel_senha = input('Escolha o nível de senha aleatória:\n1. Fraca\n2. Médio\n3. Forte\n')
comprimento = int(input('Digite o comprimento da senha: '))
match nivel_senha:
    case '1':
        print('A senha gerada é:', senha_fraca(comprimento))
    case '2':
        print('A senha gerada é:', senha_medio(comprimento))
    case '3':
        print('A senha gerada é:', senha_forte(comprimento))
