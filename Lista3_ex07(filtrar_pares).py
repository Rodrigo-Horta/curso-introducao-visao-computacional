# Crie uma função filtrar_pares que recebe uma lista de números e retorna uma nova lista 
# apenas com os números pares. Use list comprehension.

lista = []

filtrar_pares = [x for x in range(20) if x % 2 == 0]

print(filtrar_pares)
