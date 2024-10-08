#.......0123456789101112
nome = 'Everton Alves' #Iteráveis
tamanho_nome = len(nome) #conta a quantidade de caracteres
print(tamanho_nome)

indice = 0
novo_nome = ''

while indice < len(nome):
    letra = (nome[indice])
    novo_nome += f'-{letra}' #coloca o hifen antes de cada letra
    indice += 1

novo_nome += '-' #coloca um hifen no final do nome
print(novo_nome)