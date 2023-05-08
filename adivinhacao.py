from random import randrange

def adivinhacao():
    print('___'* 20)
    print("Bem vindo ao jogo de Adivinhação!")
    print('___'* 20)
    print('(1) Fácil | (2) Médio | (3) Difícil')

    nivel = int(input('Qual seu nível de dificuldade:'))

    tentativas = 3
    numero_secreto = randrange(1,11)
    rodada = 1
    pontos = 1000

    if nivel == 1:
            tentativas = 8
        
    elif nivel == 2:
        tentativas = 5
       
    else:
        tentativas = 2
    
    for rodada in range(1, tentativas + 1):
        print(f'Tentativa {rodada} de {tentativas}')
        chute = int(input('Digite seu número entre 1 e 10: '))
        acertou =  numero_secreto == chute
        maior = numero_secreto < chute
        menor = numero_secreto > chute
        
        if acertou:
            print(f'Você acertou e fez {pontos} pontos!')
            break
        
        elif chute < 1 or chute > 10:
            print('Digite um número válido.')

        else:
            
            if maior:
                print('Você errou! O seu chute foi maior que o número secreto!')
            
            elif menor:
                print('Você errou! O seu chute foi menor que o número secreto!')

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
        print('___'*20)

    print('Fim do jogo!')

if __name__ == '__main__':
    adivinhacao()


