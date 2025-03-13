#Exercício 4: Calculadora de Desconto
#Faça um programa que:

#Peça o preço original de um produto
#Peça a porcentagem de desconto
#Calcule e mostre o valor final com desconto

valor = input("Qual o valor do produto? ")
valor = float(valor)

desconto = input("Qual a porcentagem de desconto? ")
desconto=float(desconto)
descontoemreais = valor/desconto
valorcomdesconto = valor - descontoemreais
print(f"O valor do produto com desconto é: R${valorcomdesconto: .2f}")
