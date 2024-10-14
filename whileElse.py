string = 'Valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    #quando encontrar o espaço ele para o codigo e exibe até aonde foi lido até o espaço
    if letra == ' ':
        break
    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora o while.')