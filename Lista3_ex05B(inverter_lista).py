# Crie uma função inverter_lista que recebe uma lista como parâmetro e retorna uma nova 
# lista com os elementos na ordem inversa. Não use a função reverse()

lista = []
numero1= input("informe o primeiro numero da lista: ")
numero2= input("informe o segundo numero da lista: ")
numero3= input("informe o terceiro numero da lista: ")
lista.append(numero1)
lista.append(numero2)
lista.append(numero3)

print(lista)

lista_invertida = []

#função len retorna o número de itens de um objeto
#função range cria uma sequência de números. 
#range(i, j) produz i, i+1, i+2, ..., j-1. start assume o padrão 0, e stop é omitido! range(4) produz 0, 1, 2, 3
for i in range(len(lista)-1, -1, -1): 
    
    lista_invertida.append(lista[i])

print(lista_invertida)

#percorremos a lista original de trás para frente e adicionamos cada elemento em uma nova lista.
