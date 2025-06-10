def temperatura_ideal(temperatura,umidade,estacao):
    if estacao == "inverno" and temperatura >= 20 and temperatura <= 22 and umidade >= 40 and umidade <= 55:
        print('O clima está propicia para dormir...')
        
    elif estacao == "verão" and temperatura >= 23 and temperatura <=26 and umidade >= 40 and umidade <= 65:
        print('O clima está propicio para ir para à praia...')
        
    else:
        print('O clima está irregular')
        
while True:
    try:
    
        estacao = input("Digite a estação do ano(inverno/verão): ")
        temperatura = int(input('Digite sua temperatura: '))
        umidade = int(input('Digite a umidade do ar: '))
        temperatura_ideal(temperatura,umidade,estacao)
        
        
        
    except ValueError:
        print('Erro, tente novamente.')
    
    









