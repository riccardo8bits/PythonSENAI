#numero aleatório do computador
import random
#repete a ação
while True:
    print('')
    print('BEM VINDO AO JOGO!!!')
    print('JOGO DO ÍMPAR OU PAR')
    print('VOCÊ CONTRA MIM')
    print('')
    print('FAÇA SUA ESCOLHA')
    impar_par = input('Impar ou Par: ')  
    you = int(input('Digite um número: '))
    pc = random.randint(1, 10)  
    print("Número do computador foi",pc)
    #para ver se é par
    soma = you + pc
    calculo = soma % 2 == 0  
    #se sim, se não e se não se
    if impar_par == 'Par':
        if calculo:
            print('Você ganhou!')
        else:
            print('Você perdeu!')

    elif impar_par == 'Impar':
        #if não for par, ganhei
        if not calculo:
            print('Você ganhou!')
        else:
            print('Você perdeu!')

    else:
        print("Erro digite: Impar ou par")

    #perguntar se vai continuar ou não
    continuar = input("Deseja jogar novamente? (sim ou não): ")
    if  continuar == 'não':
        break
        