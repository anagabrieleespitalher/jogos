import forca
import adivinhacao

print('Escolha o seu jogo!')

print('(1) Forca | (2) Adivinhação')

jogo = int(input('Qual jogo?'))

if jogo == 1:
    print('Jogando forca')
    forca.forca()
elif jogo == 2:
    print('Jogando adivinhação')
    adivinhacao.adivinhacao()

