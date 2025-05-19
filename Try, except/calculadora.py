import inputs

def menu_calculadora():
    print("")
    print("escolha uma opção")
    print("1 - soma")
    print("2 - subtração")
    print("3 - divisão")
    print("4 - multiplicação")

menu_calculadora()


while True:
    try:
        resposta = inputs.input_int('escolha uma opção: ')

        if resposta == 1:
            n1 = inputs.input_float("digite um numero: ")
            n2 = inputs.input_float("digite outro numero: ")
            print("o resultado da soma é", n1 + n2)

        elif resposta == 2:
            n1 = inputs.input_float("digite um numero: ")
            n2 = inputs.input_float("digite outro numero: ")
            print("o resultado da subtração é", n1 - n2)

        elif resposta == 3:
            n1 = inputs.input_float("digite um numero: ")
            n2 = inputs.input_float("digite outro numero: ")
            if n2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print("o resultado da divisão é", n1 / n2)

        elif resposta == 4:
            n1 = inputs.input_float("digite um numero: ")
            n2 = inputs.input_float("digite outro numero: ")
            print("o resultado da multiplicação é", n1 * n2)

        else:
            print("Opção inválida!")

    except ValueError:
        print("Erro: Por favor, insira um número válido.")