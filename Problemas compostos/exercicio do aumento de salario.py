#Passo a Passo

#1 O novo salario
#  Quanto ele aumentou

#2 Preciso do salario com um aumneto de 10%
#  valor final do salario

#Passo1: Identificar o salario
#Passo2: multiplicar o salario por 10%
#Passo3: dividir o resultado por 100
#Passo4: Exibir o aumento do salario



salario = float(input('Digite seu salário'))
aumento = salario * 10
aumento_salario = aumento / 100
print('O seu novo salário é de ', salario + aumento_salario,'reais')
print('O aumento foi de',aumento_salario)