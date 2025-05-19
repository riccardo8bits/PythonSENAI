def menu_calculadora():
    print("")
    print("escolha uma opção")
    print("1 - soma")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")
   
menu_calculadora()

resposta = int(input('escolha uma opção'))

if resposta ==1:
    n1 = float(input("digite um numero"))
    n2 = float(input("digite outro numero"))
    print("o resultado da soma é", n1 + n2)

elif resposta == 2:
    n1 = float(input("digite um numero"))
    n2 = float(input("digite outro numero"))
    print("o resultado da soma é", n1 - n2)
   
elif resposta == 3:
    n1 = float(input("digite um numero"))
    n2 = float(input("digite outro numero"))
    print("o resultado da soma é", n1 / n2)
   
elif resposta == 4:
    n1 = float(input("digite um numero"))
    n2 = float(input("digite outro numero"))
    print("o resultado da soma é", n1 * n2)
