frase = (
    'O Python é uma linguagem de programação '
    'multiparadigma. '
    'Python foi criado por Guido van Rossum.'
)

# print(frase.count('Python')) #conta quantas vezes a palavra apareceu na string
i = 0
qtde_mais_vezes = 0
apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes = frase.count(letra_atual)

    # essa condição vai ser executada quanto a letra aparecer mais vezes que a que estou salvando nas variaveis
    if qtde_mais_vezes < quantas_vezes:
        qtde_mais_vezes = quantas_vezes
        apareceu_mais_vezes = letra_atual

        i += 1

    print(
        'A letra que apareceu mais vezes foi '
        f'{apareceu_mais_vezes} que apareceu'
        f'{qtde_mais_vezes}x'
    )
