#Tentativa de criar um jogo de forca em python
#Importa-se a biblioteca random para realizar um sorteio de palavras
import random
#Uma lista das palavras que serão sorteadas para o jogo 
palavras=['radio', 'python', 'futebol', 'guitarra', 'hipopotamo']
palavra_escolhida=random.choice(palavras)
#Utiliza-se o método join para transformar os caracteres da palavra em traços através de uma list comprehension
letras_acertadas=[indice.join(['-' if indice.isalpha() else '']) for indice in palavra_escolhida]
#Usa-se um contador para limitar as chances do usuário
cont=len(palavra_escolhida)
#Usa-se um laço while para que o usuário possa jogar várias vezes
while cont!=0:
    #Utiliza-se dict comprehension para mostrar ao usuário o seu progresso
    letras={print(f'{i}', end='') for i in letras_acertadas}
    #A variavel 'conferir' concatena cada item da lista 'letras_acertadas' formando uma só palavra
    conferir=''.join(letras_acertadas)
    #Verifica-se se o usuário chegou na resposta correta, se sim o sistema é finalizado
    if conferir==palavra_escolhida:
        print('\nMuito bom! Você acertou')       
        break
    #O usuário faz uma tentativa através da variável 'advinhe' e verifica-se se o caracter é uma letra
    try:
        advinhe=str(input('\nDigite uma letra: '))[0].strip().lower()
    except (TypeError, ValueError):
        print('ERRO! Digite uma letra')
    else:
        #Em caso de acerto ou de uma letra repetida, o usuário não perde uma tentativa
        if advinhe in letras_acertadas:
            print('Você já digitiou essa letra!')
        else:
        #Verifica-se através do for cada letra da palavra escolhida, se a tentativa 'advinhe' estiver na palavra secreta, a letra substitui o caracter '-' na respectiva posição do dicionário
            if advinhe in palavra_escolhida:
                for l in range(len(palavra_escolhida)):
                    if advinhe==palavra_escolhida[l]:
                        letras_acertadas[l]=advinhe
            else:
                cont-=1
                print(f'Letra não encontrada você tem mais {cont} tentativas')
    if cont==0:
        print(f'Não foi dessa vez! A palavra era "{palavra_escolhida}"') 


