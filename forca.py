import random

def forca():

    #mensagem de abertura
    print('___'* 20)
    print("Bem vindo ao jogo da froca!")
    print('___'* 20)

    #escolhendo as palavras de forma aleatoria com arquivo .txt
    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra = palavras[numero].lower()

    #list comprehensions para os underscores
    lista = ['_' for letra in palavra]

    #váriaveis iniciais para o while
    enforcou = False
    acertou = False
    erros = 0

    
    while not enforcou and not acertou:

        #chute do usuario
        chute = input('Escolha uma letra:').lower()
        chute = chute.strip()


        #marcação das letras, retorna os acertos e erros
        if chute in palavra:
            index = 0
            for letra in palavra:
                if chute == letra:
                    #lista puxando o index que conta cada letra
                    lista[index] = letra
                index += 1
        else:
            erros += 1     
            print("  _______     ")
            print(" |/      |    ")

            if(erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if(erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if(erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if(erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if(erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if(erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")
            print(" |            ")
            print("_|___         ")
            print()

        #variaveis que determinam quantas tentivas o usuario tem e quando acertou todas as letras
        enforcou = erros == 7
        acertou = '_' not in lista
        print(lista)

    #fora do while printa se ganhou ou perdeu
    if acertou:
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    else:
        print("Puxa, você foi enforcado!")
        print(f"A palavra era {palavra}.")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    print('Fim do Jogo!')

if __name__ == '__main__':
    forca()

