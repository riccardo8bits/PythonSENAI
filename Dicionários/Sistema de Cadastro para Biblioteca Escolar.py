livros = []

print('Sistema de Cadastro para Biblioteca Escolar')
print('')

while True:
    try:
        print('')
        print('Menu')
        print('1- ADICIONAR LIVRO')
        print('2- EXIBIR DADOS DOS LIVROS')
        print('3- EXIBIR A QUANTIDADE DE LIVROS')
        print('4- EXIBIR OS TITULOS')
        print('5- BUSCAR TODOS OS LIVROS DE UMA DETERMINADA CATEGORIA')
        print('6- PERMITIR EDITAR OS DADOS DOS LIVROS')
        print('7- BUSCAR POR AUTOR')
        print('0- SAIR')
        opcao = int(input('Digite uma opção: '))

        if opcao == 0:
            print('Fechando...')
            break
        elif opcao == 1:
            isbn = int(input('Digite o ISBN do seu livro: '))
            nome = input('Digite o nome do livro: ')
            ano = int(input('Digite seu ano'))
            autor = input('Digite o autor: ')
            categoria = input('Digite a categoria do livro: ')
            livros.append({
                
                "isbn": isbn,
                "nome": nome,
                "autor": autor,
                "categoria": categoria,
                "ano": ano
                
            })
            
            
            print('Livro cadastrado com sucesso!')

        elif opcao == 2:
            print('LIVROS:')
            for leitura in livros:
                print('')
                print("ISBN -", f"{leitura['isbn']}")
                print("NOME DO LIVRO -", f"{leitura['nome']}")
                print("ANO - ",f"{leitura['ano']}")
                print("AUTOR -", f"{leitura['autor']}")
                print("CATEGORIA -", f"{leitura['categoria']}")

        elif opcao == 3:
            quantidade = len(livros)
            print(f'Quantidade de livros: {quantidade}')

        elif opcao == 4:
            print('TÍTULOS DOS LIVROS:')
            for leitura in livros:
                print(f"TÍTULO - {leitura['nome']}")

        elif opcao == 5:
            categoria_busca = input('Digite a categoria que deseja buscar: ')
            print('LIVROS NA CATEGORIA:', categoria_busca)
            for leitura in livros:
                if leitura['categoria'] == categoria_busca:
                    print(f"TÍTULO - {leitura['nome']}")

        elif opcao == 6:
            isbn_editar = int(input('Digite o isbn do livro que deseja modificar'))
            for leitura in livros:
                if leitura['isbn'] == isbn_editar:
                    #novas categorias
                    nome = input('Diigite um novo nome: ')
                    autor = input('Digite um novo autor: ')
                    categoria = input('Digite a nova categoria: ')
                    ano = input('Digite um novo ano: ')
                    #adiciona as novas caracteristicas no dicionario
                    leitura['nome'] = nome
                    leitura['autor'] =  autor
                    leitura['categoria'] = categoria
                    leitura['ano'] = ano
                    print('dados dos livros atualizados')
                    break 
            
            
            else:
                print('Livro não encontrado.')

        elif opcao == 7:
            autor_busca = input('Digite o nome do autor que deseja buscar: ')
            print('LIVROS DO AUTOR:', autor_busca)
            for leitura in livros:
                if leitura['autor'] == autor_busca:
                    print(f"TÍTULO - {leitura['nome']}")

        else:
            print("Opção inválida! Tente novamente.")
   
    except ValueError:
        print("Error 404, Tente novamente")
