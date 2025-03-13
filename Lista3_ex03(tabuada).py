# Crie uma função criar_tabuada que recebe um número como parâmetro e retorna 
# uma lista com a tabuada desse número (de 1 a 10). Use um loop while.

#Tabuada de Multiplicação ( de 1 a 10)
numero= int(input('Tabuada de : '))
# num = int(input("Display multiplicação
for i in range(1, 11):
 print(numero, 'x', i, '=', numero*i)
