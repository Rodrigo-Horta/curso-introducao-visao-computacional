#Desenvolva uma função contar_vogais que recebe uma string e retorna o número de vogais. Use um loop for 
# e condicionais para verificar cada caractere.

def contarvogais():
    i = 0
    j = 0
    string = str (input("Digite uma palavra: "))
    for i in string:
        if (i == 'A' or i == 'a'
        or i == 'E' or i == 'e'
        or i == 'I' or i == 'i'
        or i == 'O' or i == 'o'
        or i == 'U' or i == 'u'):
             j+=1
    print("A palavra que digitou tem", j, "vogais: ")
contarvogais()
