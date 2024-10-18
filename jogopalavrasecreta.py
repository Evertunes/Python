"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os
palavra_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0
while True:
    
    letra_digitada = input('Digite uma letra: ')
    #entrou no laco, começa a contar tentativas
    numero_tentativas += 1
    
    #se o usuario digitar mais de uma letra, exibe a msg de erro
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    #verifica se a letra digitada está em nossa palavra secreta
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada #concatena a letra digitada na variavel letras_acertadas
    palavra_formada = ''
    #joga a varivavel letra_secreta em falavra formada se a letra estiver entre as letras acertadas
    #senão exibe *
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
            
    if numero_tentativas > len(palavra_secreta) and letra_digitada not in palavra_secreta:
        os.system('clear')
        print('Numero de tentativas excedidas... Tente de novo!')
        numero_tentativas = 0
        palavra_formada = 0
        continue
    
    print('Palavra formada: ', palavra_formada)
    
    if palavra_formada == palavra_secreta:
        os.system('clear') #limpa o terminal
        print('VOCE GANHOU!! PARABENS!')
        print('A palavra era ', palavra_secreta)
        print('Tentativas: ', numero_tentativas)
        #zera tudo
        letras_acertadas = ''
        numero_tentativas = 0