
def soma( a, b):
    num1 =  a
    num2 =  b
    res = a + b
    print("soma de {} + {} é igua a {}".format(a,b, res))


def subtracao():
    a = int(input("Digite o numerador: "))
    b = int(input("Digite o numerador: "))
    return  a - b


####PROGRAMA PRINCIPAL
print("################################################")
print("BEM VINDO AO TABUADA")
print("################################################")

a = int(input("Digite o numerador: "))
b = int(input("Digite o numerador: "))

soma(a, b)

print("#########################################################")

sub = subtracao()
print("o resultado da subtração é: {} ".format(sub))






















