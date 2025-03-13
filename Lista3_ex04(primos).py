# Implemente uma função verificar_primo que recebe um número e retorna True se for primo e 
# False caso contrário. Use um loop for e condicionais.

# numeros primos
number = input("Forneça um numero: ")
number = int(number)

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
elif number == 0:
    print(number, 'é zero')
elif number == 1:
    print(number, 'é um')
else:
    print(number, 'é negativo')
