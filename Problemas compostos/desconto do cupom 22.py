#Passo a Passo

#1  novo preco do produto
#   quanto diminuiu

#2 nome do produto e o preco
#  um desconto de 5%
#  novo preco
#  quanto o valor do produto diminuiu

#3
#Passo1 qual o nome do produto
#Passo2 o valor do produto
#Passo3 adicionar o cupom de desconto no produto
#Passo4 exibir o valor do produto com desconto
#Passo  Subtrair o valor desconto pelo preco

        
produto = input('Digite qual é o nome do produto')
preco = float(input('Qual o preco do produto?'))
cupom = preco * 5
cupom1 = cupom / 100
print('O valor do desconto é de',cupom1)
print('O valor do produto com desconto é de ', preco - cupom1)