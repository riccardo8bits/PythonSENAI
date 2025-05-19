#Dicionários





#Criar
aluno = {
    "nome": "Ricardo",
    "idade": 16,
    "altura": 1.69,
    "Matriculado": True 
    
    
}


carro = {
    "carro": "Honda Civic Typer R 97",
    "motor": "motor B16B",
    "ano": 1997
}

carro2 = {
    "carro": "Toyota Supra MK4",
    "motor": "motor 2jz-GTE",
    "ano": 1993


}

carro3 = {
    "carro": "Astra OPC Nürburgring Edition",
    "motor": "motor V8 de 4.0 litros, com 460 cv",
    "ano": 2003
    
    
    
}


#Adicionar campo

aluno["peso"] = 61




#Alterar campo
aluno["idade"] = 17




#Deletar campo

del aluno["altura"]







    
    
    
    
    
    
#Exibir
    

    
    
#Exibir uma lista de Dicionários
lista_carro = [carro,carro2,carro3]
    
    
    




#Exibindo todos
    
for carro in lista_carro:
    for chave, valor in carro.items():
        print(f'{chave}: {valor}')
    print('')
    print('')
    
    
    

    
    
    
    
