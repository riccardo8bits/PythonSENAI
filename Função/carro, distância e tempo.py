distancia = float(input('Qual é a distância do percurso em km: '))
velocidade = float(input('Digite a velocidade em km/h: '))
def conta(distancia, velocidade):
    r = distancia / velocidade
    
    print('Para percorre um percurso de {} km com a velocidade de {} km/h vai demorar {} horas '.format(distancia,velocidade,r))

conta(distancia,velocidade)
