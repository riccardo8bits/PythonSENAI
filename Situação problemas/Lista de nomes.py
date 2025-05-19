import inputs



lista = []

while True:
    print('')
    print('')
    print('MENU:')
    print('')
    print('[1]- cadastra nomes')
    print('[2]- exibir o total de inscritos')
    print('[3]- exibir a lista de nomes em ordem alfabética')
    print('[4]- permitir a consulta de um nome')

    escolha = inputs.input_int("digite sua escolha: ")

    if escolha == 1:
        nome = inputs.input_str('digite seu nome: ')
        if nome in lista:
            print('este nome já está na lista')
        else:
            lista.append(nome)
            print("nome cadastrado")
    elif escolha == 2:
        print('O total de inscritos é de', len(lista))
       
    elif escolha == 3:
        lista.sort()
        print('')
        print('LISTA DOS NOMES:')
        for nome in lista:
            
            print(nome)
    elif escolha == 4:
        nome = inputs.input_float('digite o nome para consulta: ')
        if nome in lista:
            print("nome encontrado! deseja remove-lo (s/n)")
            resposta = inputs.input_str('Digite sua resposta: ')
            if resposta == 's':
                lista.remove(nome)
                print("nome removido")
            else:
                print("nome não removido.")
        else:
            print("nome não encontrado.")
            adicionar = inputs.input_str("Deseja adicionar este nome a lista? (s/n) ")
            if adicionar == 's':
                lista.append(nome)
                print("nome cadastrado com sucesso")
