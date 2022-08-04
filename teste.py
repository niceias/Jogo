from shlex import join

num = 0
clientes = []
while(num <= 1):
    with open('palavrasecreta', 'a', newline="") as arquivo:
        nome = input("digite o seu nome: ")
        cpf = input("digite o cpf: ")
        idade = input("Digite a idade: ")
        num += 1
        cliente = (nome, cpf, idade)
        arquivo.write(join(cliente))
        arquivo.write('\n')

    clientes.append(cliente)

for i in clientes:
    print(i)



















