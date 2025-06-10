notas = []
def media(nota1,nota2,nota3):
    mediaa = (nota1 + nota2 + nota3) / 3
    mediaa1 = (nota1 + nota2 + nota3) // 3
    
    resto = mediaa - mediaa1
    
    if resto >= 0.3 and resto <= 0.5:
        return mediaa1 + 0.5
    if resto < 0.3:
        return mediaa1 + 0
    if resto >= 0.5 and resto <=0.7:
        return mediaa1 + 0.5
    if resto >= 0.8 and resto <= 0.9:
        return mediaa - resto + 1   
    
    
    
def verificar_media(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperação"
    if media < 5:
        return "Reprovado"
    
def menu():
    print('1- Cadastrar o aluno')
    print('2- Relatório')
    print('3- Sair do aplicativo')
    
    
def condicoes(opcao):
    if opcao == 1:
        nome = input('Digite seu nome: ')
        nota1 = float(input('Digite a sua primeira nota: '))
        nota2 = float(input('Digite a sua segunda nota: '))
        nota3 = float(input('Digite a sua terceira nota: '))
        mediaa = media(nota1,nota2,nota3)
        situacao = verificar_media(mediaa)
        notas.append({
            "nome": nome,
            "mediaa": mediaa,
            "situacao": situacao
            })
    elif opcao == 2:
        print('NOMES-NOTAS-APROVADOS-REPROVADOS')
        print('')
        for testes in notas:
            print("nome -",f"{testes['nome']}")
            print("media - ",f"{testes['mediaa']}")
            print("situacao -",f"{testes['situacao']}")
    
while True:
    menu()
    print('')
    opcao = int(input('Digite a sua opção: '))
    print('')
    condicoes(opcao)
    print('')
    if opcao == 3:
        print('Fechando...')
        break
    
        
        
        
        
        
        
        
        
        
        
        