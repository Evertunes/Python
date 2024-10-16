qtde_linhas = 5
qtd_colunas = 2

linha = 1

while linha <= qtde_linhas:
    coluna = 1

    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}') #colocar as variaveis em fstring f'{var=}exibe o nome da varivel e o valor da variavel
        coluna += 1

    linha += 1

print('Acabou')
