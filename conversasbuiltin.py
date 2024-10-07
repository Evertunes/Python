string = " everton alves"

#outra_variavel = f'{string[:3]}ABC{string[4:1]}'
#print(string)
#print(outra_variavel)
print(string.zfill(100))#se minha string não tem 100 caracteres o python preenche o restante com 0
print(string.capitalize()) #deixa a primeira letra da string Maiúscula
print(string.islower()) #retorna true se todos os caracteres forem minusculos, e false caso contrário

