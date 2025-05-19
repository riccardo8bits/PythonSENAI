triangulo1 = int(input('Qual é o lado do seu triângulo? '))
triangulo2 = int(input('Qual é o outro lado do seu triângulo? '))
triangulo3 = int(input('Qual é o ultimo lado do seu triângulo? '))

if triangulo1 == triangulo2 == triangulo3:      
    print('Triângulo equilátero')
elif triangulo1 == triangulo2 or triangulo2 == triangulo3 or triangulo1 == triangulo3:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')
