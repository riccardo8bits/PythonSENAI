def input_int(mensagem="Digite um inteiro: "):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            
def input_float(mensagem = "Digite um número com casas decimais: "):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número com casas decimais.")

def input_str(mensagem="Digite uma string: "):
    return input(mensagem)
