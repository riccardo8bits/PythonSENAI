ano = int(input('Qual é seu ano de nascimento? '))
ano_atual = 2025
idade = ano_atual - ano

if ano > ano_atual:
    print('Você ainda não nasceu.')
elif idade > 115:
    print('Idade inválida.')
elif idade <= 10:
    print('Você é uma criança.')
elif 11 <= idade <= 17:
    print('Você é um adolescente.')
elif 18 <= idade <= 59:
    print('Você é um adulto.')
else:
    print('Você é um idoso.')