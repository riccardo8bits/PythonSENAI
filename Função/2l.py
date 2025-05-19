def menu_calculadora():
    print('')
    print('Escolha uma opção')
    print('1 - soma')
    print('2 - subtração')
    print('3 - divisão')
    print('4 - multiplicação')
    
menu_calculadora()

resposta = int(input('Escolha uma opção: '))

if resposta == 1:
    n1 = float(input('Digite um numero para somar: '))
    n2 = float(input('Digite outro numero para somar: '))
    print('Seu resultado é ',n1 + n2)
    
elif resposta == 2:
    n1 = float(input('Digite um numero para subtrair: '))
    n2 = float(input('Digite outro numero para subtrair: '))
    print('Seu resultado é ',n1 - n2)
    
elif resposta == 3:
    n1 = float(input('Digite um numero para dividir: '))
    n2 = float(input('Digite outro numero para dividir: '))
    print('Seu resultado é ',n1 / n2)
    
elif resposta == 4:
    n1 = float(input('Digite um numero para multiplicar: '))
    n2 = float(input('Digite outro numero para multiplicar: '))
    print('Seu resultado é ',n1 * n2)
    
    
    
    