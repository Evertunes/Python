"""
#Exercicio 1

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
#----------------------------------------------------------------------------------------------
"""
#Exercicio 1

numero_str = input("Digite um numero inteiro: \n")

try:
    numero_int = int(numero_str)
    
    if (numero_int % 2 == 0):
        print("O numero: %i" % (numero_int), "é par!")
    else:
        print("O numero: %i" % (numero_int), "não é par!")
except:
    print('Isso não é um número')
"""
#----------------------------------------------------------------------------------------------
"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada) #converte o input str em inteiro

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Bom tarde')
    elif hora >= 18 and hora <= 23:
        print('Bom noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')
"""
#----------------------------------------------------------------------------------------------

nome = input('Digite seu nome: ')
tamanho_nome = len(nome) #faz a contagem de caracteres

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')