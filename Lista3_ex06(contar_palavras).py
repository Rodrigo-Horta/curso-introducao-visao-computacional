# Desenvolva uma função contar_palavras que recebe uma string e retorna um dicionário onde 
# as chaves são as palavras e os valores são a quantidade de vezes que cada palavra aparece.

frase = []
frase = input("informe uma frase: ")
contar_palavras = frase.count("digo")
print("a palavra digo aparece", contar_palavras, " vez(es)")

palavras = frase.split()
contagem = len(palavras)
print(contagem)
