import random

def jogar():
    print("###############################")
    print("Bem vindo ao jogo de advinhação")
    print("###############################")

    #random.seed(99)
    numer_secreto = random.randrange(1,101)
    print(numer_secreto)
    tentativas = 0
    rodada = 1
    pontos = 1000


    print("Qual o nivel de dificuldade?")
    print("(1) Fácil (2) Média (3) dificil")
    nivel = int (input("defina um nivel:"))


    if(nivel==1):
        tentativas = 20
    elif(nivel==2):
        tentativas = 10
    else:
        if(nivel==3):
            tentativas = 3
        elif(nivel<0 or nivel > 3):
            print("Valor invalido, reinicie o jogo!")



    for rodada in  range(1, tentativas + 1):
        print("tentiva {} de {}". format(rodada, tentativas))
        chute_str = input("digite um numero")
        print("voce digitou", chute_str)
        chute= int(chute_str)


        if(chute < 1 or chute > 99):
            print("digite um valor entre 1 e 99")
            continue

        acertou = chute == numer_secreto
        maior = chute > numer_secreto
        menor = chute < numer_secreto

        if(acertou):
            print("voce acertou e fez {}". format(pontos))
            print("fim de Jogo!")
            break
        else:
            if(maior):
                 print("voce errou! O seu numero foi maior que o numero secreto")
            elif(menor):
                 print("voce errou! O seu numero foi menor que o numero secreto")

                #cauculo dos pontos ganhos
            pontos_perdidos = abs(numer_secreto - chute)  #40-20 = 20
            pontos = pontos - pontos_perdidos


    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()

