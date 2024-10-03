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

data_entrada = input ("Digite a data atual: ")
data = [entrada[]]
try:
    data = int(data)
    
    if(data >= 0 and data <= 11):
        print("Bom dia!")
    if(data >= 12 and data <= 17):
        print("Boa tarde!")
    if(data >= 18 and data <= 23):
        print("Boa noite!")
except:
    print("Data Inválida!")