import advinhacao
import forca


print("################################")
print("***Escolha o seu Jogo***")
print("################################")


print("(1) Advinhação (2) Forca")
jogo = int (input('Qual o jogo deseja jogar?'))

if (jogo ==1):
    print('Jogo da advinhação')
    advinhacao.jogar()
elif(jogo == 2):
    print('Jogo da Forca')
    forca.jogar()

if(__name__ == "__main__"):
    jogar()
