import random
pc = random.randint(0, 100)  
    

print("")
print("BEM-VINDO AO JOGO DE ADIVINHAÇÃO")
print("")
print("Sou seu computador e estou pensando em um número entre 0 e 100.")
print("Tente adivinhar qual é esse número")
print("")


    
while True:
    palpite = int(input("Digite seu palpite: "))  
    if palpite > pc:
        print('O número é menor que', palpite)
    elif palpite < pc:
        print('O número é maior que', palpite)
    elif palpite == pc:
        print('Você acertou!')
        print('1 - Para sair')
        print('2 - Para continuar')
        continuar = int(input('Digite sua escolha: '))  
            
        if continuar == 2:
            print("Vamos jogar novamente!")
            pc = random.randint(0, 100)
            
                
        else:
            print("Jogo fechando...") 
            break  