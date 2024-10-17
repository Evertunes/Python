"""
    Iteravel -> str, range, etc(__iter__) #Entrega um elemento por vez da String
    Iterador -> quem sabe entrear um valor por vez
    FOR + Rangue
    range -> range(start, stop, step)

texto = iter('Luiz') #me entra o objeto iterador

print(next(texto)) #next chama o proximo valor disponivel dentro do iter(string)
    """

texto = 'Everton'
iterator = iter(texto)

while True:
    try:
        print(next(iterator))
        
    except StopIteration: #quando der o erro de fim de iteração, quando não tem mais valor ele para o codigo
        break