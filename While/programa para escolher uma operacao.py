while True :
    print("MENU")
    print("")
    print("[1]-FATORIAL")
    print("[2]-QUADRADO")
    print("[3]-CUBO")
    print("[4]-TABUADA")
    print("[0]-SAIR")
    escolha = int(input("Faça sua escolha: "))
    if escolha == 0:
        break
    elif escolha == 1:
        num = int(input("digite um numero"))
        fatorial = 1
        while (num > 0 ):
            fatorial = fatorial*num
            num = num - 1
            print("o fatorial do numero é", fatorial)
           
       
    elif escolha == 2:
        num = int(input("digite um numero para saber seu quadrado"))
        resultado = num*num
        print("o quadrado é", resultado)
       
    elif escolha == 3:
        num = int(input("digite um numero para saber seu cubo"))
        resultado = num*num*num
        print("o resultado do cubo é", resultado)
       
    elif escolha == 4:
        num = int(input("digite um numero para saber sua tabuada"))
        print(num, 'X 1 =', num*1)
        print(num, 'X 2=', num*2)
        print(num, 'X 3 =', num*3)
        print(num, 'X 4 =', num*4)
        print(num, 'X 5 =', num*5)
        print(num, 'X 6 =', num*6)
        print(num, 'X 7 =', num*7)
        print(num, 'X 8 =', num*8)
        print(num, 'X 9 =', num*9)
        print(num, 'X 10 =', num*10)
