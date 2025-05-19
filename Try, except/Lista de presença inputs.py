import inputs

#Controle de presença
nomes_savos = []
presentes = []
ausentes = []


print('')
print('1- Cadastro de nomes')
print('2- Exibir total de pessoas')
print('3- Exibir em ordem de cadastro')
print('4- Confirmação de presença')
print('5- Relatório da lista de presença')
print('6- Sair')
print('')
print('')

while True:
    opcao = inputs.input_int('Digite sua opção: ')

    if opcao == 1:
        name = inputs.input_str('Digite seu nome: ')
        if name in nomes_savos:
            print('O nome [',name,'] já está na lista...')
        else:
            print('Nome cadastrado com sucesso...')
            nomes_savos.append(name)

    elif opcao == 2:
        print('O total de nomes na lista é de ',len(nomes_savos),' pessoas...')

    elif opcao == 3:
        for name in nomes_savos:
            print('{}'.format(name))

    elif opcao == 4:
        print("Confirmando presença...")
        presentes = []
        ausentes = []
        for name in nomes_savos:
            pergunta = inputs.input_str(name +  'está presente?(s/n) ')
            if pergunta == 's':
                presentes.append(name)
            elif pergunta == 'n':
                ausentes.append(name)

    elif opcao == 5:
        print('Presentes:')
        for nome in presentes:
            print(nome)
        print('Ausentes:')
        for nome in ausentes:
             print(nome)

    elif opcao == 6:
        print('Fechando...')
          
