nome = input('Qual o seu nome? ')
print(f'Seja bem-vindo {nome}', end='\n')
print('===================================')
print('Agora por favor...', end='\n')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

#aqui eu faço uma checagem para garantir que o que eu digitei são numeros inteiros
#converto a entrada em INT, para garantir a soma, se não for numero inteiro, gera um erro ao final do codigo
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1 + int_numero_2}')
