notas = []

def menu():
    print('SISTEMA DE NOTAS DE ALUNOS: ')
    print('')
    print('')
    print('1- ADICIONAR NOTAS')
    print('2- VISUALIZAR NOTAS DOS ALUNOS EM RECUPERAÇÃO')
    print('3- VISUALIZAR NOTAS DOS ALUNOS APROVADOS')
    print('4- NOMES DOS ALUNOS APROVADOS')
    print('5- NOMES DOS ALUNOS DESAPROVADOS')
    
    print('')

    
    
def condicao_adicionar_notas(opcao):
    if opcao == 1:
        name = input('Digite o nome do aluno: ')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        media = (nota1 + nota2 + nota3) / 3
        print('')
        
        
        print('Nome e notas cadastradas')
        print('')
        print('')
        notas.append({
            
            
            "name": name,
            "media": media,
            
            
            
            
            
            
            })
        
def notas_all(opcao):
    
    if opcao == 2:
        
        print('NOMES-NOTAS-APROVADOS-REPROVADOS')
        print('')
        
        for testes in notas:
            print("nome -",f"{testes['name']}")
            print("media - ",f"{testes['media']}")
            
            print('')
        
    
        
        
        
        
        
        
        
while True:
    
    menu()
    
    opcao = int(input('Digite sua opção: '))
    condicao_adicionar_notas(opcao)
    notas_all(opcao)
        
            
        
            
        
        
        
        