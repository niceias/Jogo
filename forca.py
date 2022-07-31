import random
def jogar():
    print("################################")
    print("***Bem vindo ao jogo de forca***")
    print("################################")

    #teste do github

    #arquivo = open ("palavrasecreta", "r")
    #palavras = []

    #for linha in arquivo:
        #linha = linha.strip()
        #palavras.append(linha)

    #arquivo.close()
    #teste no github
    with open("palavrasecreta", "r") as arquivo:
        palavras = []
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()


    letras_acertadas = ['_' for letra in palavra_secreta] #list Comprehensions

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = input('Qual a Letra?')
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                   letras_acertadas[index] = letra
                index += 1

        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6 - erros))


        enforcou = erros == 6
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print('Você ganhou')
    else:
        print("Você perdeu")

    print('fim do Jogo!')


if(__name__ == "__main__"):
    jogar()

