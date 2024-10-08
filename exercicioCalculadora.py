"""Calculadora com while"""
while True:
    sair = input('Quer sair? [s]im: ').lower().startswith('s')#retorna a mesma string eniada em sair em letra minuscula/startswitch verifica que o que a pessoa digitou começa com a letra desejada
    
    if sair is True:
        break