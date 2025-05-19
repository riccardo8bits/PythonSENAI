# Colocando itens na lista
veiculos = ['Aviões', 'Carros', 'Barcos']

# Adiciona mais um objeto na lista
veiculos.append('Submarinos')
print('O veículo adicionado: Submarinos')

print('')
print('')

# Acessa o objeto que está na opção 2 e exibe
print('O item da segunda opção é o', veiculos[1])

print('')
print('')

# Remoção do item e a exibição
veiculo_removido = veiculos.pop(1)
print('O veículo removido foi:', veiculo_removido)

print('')
print('')

# Quantidade de itens na lista
quantidade = len(veiculos)
print('A quantidade de itens na sua lista é de', quantidade)

print('')
print('')

# Mostrar todos os itens
if "Cadeira" in veiculos:
    veiculos.remove("Cadeira")
else:
    veiculos.append('Cadeira')

# Ordenar a lista em ordem alfabética, exibir depois
veiculos.sort()
print('A lista de veículos em ordem alfabética é:', veiculos)

print('')
print('')

# Exiba o primeiro e o último item da lista
if len(veiculos) > 0:
    primeiro_item = veiculos[0]
    ultimo_item = veiculos[-1]
    print('O primeiro item é:', primeiro_item)
    print('O último item é:', ultimo_item)
else:
    print('A lista está vazia, não há itens para mostrar.')

print('')
print('')

# Limpar a lista
veiculos.clear()
print('A lista foi limpa. Agora ela está vazia:', veiculos)