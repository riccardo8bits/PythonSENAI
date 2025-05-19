#digite um numero ao usuario e exiba todos os numeros pares e a quantidade deles até o numero solicitado
num = int(input("digite um numero: "))
quantidade = 0
print(num)
while True :
    num = num - 1
    if num % 2 == 0:
        print(num)
        quantidade = quantidade + 1
    elif num <=0:
        print("a quantidade de numeros pares é", quantidade )
        break
