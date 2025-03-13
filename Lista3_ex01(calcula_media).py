#Crie uma função chamada calcular_media que recebe uma lista de números como parâmetro e retorna a média. 
#Use um loop for para somar os números.

# Exemplo de uso:
#notas = [7.5, 8.0, 6.5, 9.0]
#media = calcular_media(notas)

notas = [7.5, 8.0, 6.5, 9.0]
calcular_media = 0

for nota in notas:
    calcular_media += nota

print(calcular_media/4)
