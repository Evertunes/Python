"""
    Repetições
    While(enquanto)
    Exeuta uma ação enquanto uma condição for verdadeira
    
"""
"""
while condicao:
    nome = input('Qual o seu nome: \n')
    print('------------------')
    print(f'Seu nome é {nome}')
    print('------------------')

    if nome == 'sair':
        break

print('Acabou')
"""
"""
contador = 0

while contador < 10:
    contador = contador + 1 #conta de um em um até 10 e finaliza o codigo
    print(contador)
    
print('ACABOU')

"""    

#--------------------------------------------------------------------------

"""
    
    Operadores de atribuição
    
    = += -= *= /= //= **= %=
    
"""

contador = 0
while contador <= 10:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue #pula o numero 6 e vota no while
    
    print (contador)    
    
    if contador == 40:
        break
    
print ('ACABOU  ')