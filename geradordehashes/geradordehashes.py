import hashlib

string = input('Digite o texto que irá receber o hash: ')

resultado = hashlib.md5(string.encode('utf-8'))

print('O hash gerado é: ', resultado.hexdigest())

