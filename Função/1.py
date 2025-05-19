from datetime import datetime

def saudacao(nome):
    hora = datetime.now().hour
    if hora <= 6:
        print('Boa madrugada',nome)
    elif hora <= 12:
        print('Bom dia',nome)
    elif hora <= 20:
        print('Boa tarde',nome)
    else:
        print('Boa noite',nome)
    
nome = input('Qual é seu nome: ')
saudacao(nome)
        
        