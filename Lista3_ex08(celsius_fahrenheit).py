# Implemente uma função celsius_para_fahrenheit que recebe uma lista de temperaturas em Celsius 
# e retorna uma lista com as temperaturas convertidas para Fahrenheit. Use list comprehension.

temperaturas = [ 12, 21, 15, 32] 
celsius_para_fahrenheit = [temperatura * 9/5 + 32 for temperatura  in temperaturas]
print(celsius_para_fahrenheit)

texto = 'olá mundo    :'
print(texto.strip())
