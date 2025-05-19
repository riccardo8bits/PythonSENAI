nota1 = int(input('Qual é a nota do 1 aluno'))
nota2 = int(input('Digite a nota do 2 aluno'))
media = (nota1 + nota2) /2

if nota1 > 0 and nota1 < 100 and nota2 > 0 and nota2 < 100:
    
    if media >= 70:
        print('AProvado')
    elif media >= 50 and media <= 70:
        print('Recuperação')
    elif media < 50:
        print('Recuperação')
else:
    print('Erro, não ultrapasse o 100')