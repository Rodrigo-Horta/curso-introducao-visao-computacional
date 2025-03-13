#Exercício 5: Conversor de Moedas
#Desenvolva um programa que:

#Peça um valor em reais
#Converta para dólares (use uma taxa fixa, por exemplo, 5.00)
#Mostre o resultado formatado com duas casas decimais

reais = input("Informe o valor em reais: R$")
reais = float(reais)
taxa = 5
dolares = reais*taxa

print(f"Esse valor em dóalres é ${dolares: .2f}")
