"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input ('Digite seu nome: \n')
print(16*'-')
idade = input ('Digite sua idade: \n')
print(16*'-')
nomeinverte = nome[::-1]
espaco = " "

if nome != '' and idade != '':
    print ('Nome: %s'%(nome))
    print(16*'=')
    print ('Nome invertido: %s ' % (nomeinverte))
    print(16*'=')
    if espaco in nome:
        print("Tem espaços no seu nome!")
    else:
        print("Seu nome não possui espaços!")

