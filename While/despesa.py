total_despesa = 0
quantidade_despesa = 0

while True :
    print("Opções")
    print("[0]- Sair")
    print("[1]- Adicionar Despesa")
    print("[2]- Mostrar quantidade de despesa")
   
    escolha = int(input("Faça sua escolha"))
    if escolha ==0:
        break
    elif escolha ==1:
        opcao = int(input("adicione o valor da sua despesa"))
        total_despesa = total_despesa + opcao
        quantidade_despesa = quantidade_despesa + 1
    elif escolha ==2:
        print("quantidade de despesa", quantidade_despesa)
        print("valor total", total_despesa)