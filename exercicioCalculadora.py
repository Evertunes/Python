'''Calculadora com while'''
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    num1_float = 0
    num2_float = 0
    
    #validação se o número é valido, senão o 'continue' volta no começo para receber um ou mais numeros validos
    try:
        num1_float = float(numero_1)
        num2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador Inválido!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    print('Realizando sua conta. confira o resultado abaixo: ')
    
    if operador == '+':
        print(f'{num1_float}+{num2_float}=', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float}-{num2_float}=',num1_float - num2_float)
    elif operador == '/':
        print(f'{num1_float}/{num2_float}=',num1_float / num2_float)
    elif operador == '*':
        print(f'{num1_float}*{num2_float}=',num1_float * num2_float)
    else:
        print('Nunca deveria chegar aqui.')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')#retorna a mesma string eniada em sair em letra minuscula/startswitch verifica que o que a pessoa digitou começa com a letra desejada
    
    if sair is True:
        break