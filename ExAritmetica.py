nome = 'Everton Alves'
altura = 1.66
peso = 70
imc = peso / (altura * altura)

# print(nome, '\n' 'Peso:', peso, '\n' 'Tem:', altura, '\nSeu IMC e: ', imc)
# impressao com f-string
linha_1 = f'{nome} tem {altura:.1f} de altura' #.1f formata com 1 casa decimal
linha_2 = f'pesa {peso} quilos e seu IMC e: '
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)