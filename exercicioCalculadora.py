"""Calculadora com while"""
while True:
    sair = input('Quer sair? [s]im: ')
    sair = sair.lower().startswith('s') #retorna a mesma string eniada em sair em letra minuscula/startswitch verifica que o que a pessoa digitou começa com a letra desejada
    print(sair)