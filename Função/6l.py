def Calculo_IMC(peso, altura):
    return peso / (altura * altura)
   
def Resultado(Imc):
    print("O IMC encontrado é {:.2f}".format(Imc))

def tabela_IMC(imc):
    Resultado(imc)
    if imc < 18.5:
        print("Magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print("Normal")
    elif imc >= 25.0 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30.0 and imc <= 34.9:
        print("Obesidade grau 1")
    elif imc >= 35.0 and imc <= 39.9:
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3")
   
altura = float(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))
imc = Calculo_IMC(peso, altura)

tabela_IMC(imc)