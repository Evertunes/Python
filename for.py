texto = 'Python'
novo_texto = ''
#varivavel letra é criada no for
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')
