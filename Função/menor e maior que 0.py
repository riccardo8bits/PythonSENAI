def positivo(pergunta):
    if pergunta >= 0:
        print('o numero {} é positivo.'.format(pergunta))
        print('')
def negativo(pergunta):
    if pergunta < 0:
        print('o numero {} é negativo.'.format(pergunta))
        print('')
        
while True:
    try:
    
        pergunta = int(input('Digite seu numero: '))

        positivo(pergunta)
        negativo(pergunta)
        
    except ValueError:
        print('Erro, tente novamente...')
        print('')

        
    
    



