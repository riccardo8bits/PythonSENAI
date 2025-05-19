def conversor(you):
    #multiplique a temperatura em Celsius por 1,8 e some 32 ao resultado
    converter_fahrenheit = (you * 1.8) + 32
    converter_kelvin = you +  273
    
    
you = float(input('Qual é se numero'))
conversor(you)
print('A conversão para fahrenheit é de {}',format(conerter_fahrenheit))
    
    