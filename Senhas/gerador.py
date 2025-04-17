import random
import string

def senha_letras(comprimento):
    caracteres = string.ascii_letters
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_numeros(comprimento):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

def senha_simbolos(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for caracter in range(comprimento))
    return senha

nivel_senha = input('Escolha os critérios da senha aleatória:\n1. Apenas letras\n2. Letras e números\n3. Letras, números e caracteres especiais\n')
comprimento = int(input('Digite o comprimento da senha: '))
match nivel_senha:
    case '1':
        print('A senha gerada é:', senha_letras(comprimento))
    case '2':
        print('A senha gerada é:', senha_numeros(comprimento))
    case '3':
        print('A senha gerada é:', senha_simbolos(comprimento))
