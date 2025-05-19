numero1 = float(input('Digite um numero: '))
numero1 = float(input('Digite outro numero: '))

def menu_calculadora():
    print('')
    print('Escolha uma opção')
    print('1 - soma')
    print('2 - subtração')
    print('3 - divisão')
    print('4 - multiplicação')
    
menu_calculadora()

opcao = int(input('Qual é sua escolha: '))



def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def divisao(numero1, numero2):
    return numero1 / numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def Conta_secolhida():
    if opcao == 1:
        print('O resultado da soma é',soma(numero1, numero2))
    elif opcao == 2:
        print('O resultado da subtração é',subtracao(numero1, numero2))
    elif opcao == 3:
        print('O resultado da soma é',divisao(numero1, numero2))
    elif opcao == 4:
        print('O resultado da soma é',multiplicacao(numero1, numero2))
        





