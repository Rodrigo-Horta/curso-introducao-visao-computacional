num = input("Forneça um número: ")

while num <= 10:
    i = 1
    while i <= 10:
        product = num*i
        print(num, " * ", i, " = ", product, "\n")
        i = i + 1
    num = num + 1
    print("\n")
