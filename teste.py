
def ler_arquivo():
    with open("palavrasecreta", "r") as arquivo:
        linha = arquivo.read()
        print(linha)



def escreve_arquivo():
   pedido = "s"
   while(pedido == "s"):
        with open("palavrasecreta", "a", newline="") as arquivo:

            arquivo.write(input("Digite aqui: "))
            arquivo.write('\n')

        pedido = input("deseja continuar pedindo: ")



def captura_arquivo():
    with open("palavrasecreta", "r") as arquivo:
        lista = []
        for linha in arquivo:
            linha =  linha.strip()
            lista.append(linha)
        print(lista)


leitura = int(input("Digite uma opção: "))

if(leitura == 1):
    ler_arquivo()
elif(leitura == 2):
    escreve_arquivo()
else:
    captura_arquivo()















