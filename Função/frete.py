peso = int(input('Digite o peso da carga em kg: '))
distancia = int(input('Digite a distância: '))
print('Taxa: 20R$')
def calculo(peso,distancia):
    valor = (peso * 0.5) + (distancia * 0.1) + 20
    print('Preço total da viagem é de {}R$'.format(valor))
    
calculo(peso,distancia)
