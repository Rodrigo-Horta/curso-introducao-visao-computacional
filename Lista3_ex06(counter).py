frase = []
frase = input("informe uma frase: ")

from collections import Counter
contagem_palavras = Counter(frase)
print(contagem_palavras)
