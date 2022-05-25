from random import choice
from time import sleep
Temas = {
    "cores": ["magenta", "ciano", "esmeralda", "chumbo"],
    "frutas": ["acerola", "goiaba", "graviola", "abacate"],
    "animais": ["macaco", "tigre", "veado", "rato"]
}

print('>' * 20, 'UNIESP', '<' * 20)
print('Grupo:\nJoão Pedro de Souza Pires E-mail: 2022111510112@iesp.edu.br \nBernardo Meister Gehrke - E-mail: 2022111510012@iesp.edu.br ')
print(' ' * 16, 'Jogo da Forca!')
print('=' * 48)
print('E ai, vamos jogar um Jogo da Forca??')
jogar = str(input("Sim ou Não: ")).strip().upper()

if jogar in 'SIM':
    while True:
        print('''Jogo da Forca
Temas: 
1 - Cores 
2 - Frutas 
3 - Animais 
4 - Sair do Jogo''')
        option = str(input('Escolha uma opção: '))
        if option == '4':
            print('Saindo do jogo...')
            break
        elif option == '1':
            palavra = choice(Temas['cores'])
        elif option == '2':
            palavra = choice(Temas['frutas'])
        elif option == '3':
            palavra = choice(Temas['animais'])
        print('Voce tem 10 chances para acertar a palavra! Boa sorte! xD')
        print('Pensando em palavra...')
        sleep(3)
        print('Palavra escolhida com sucesso!')
        tentativas = ["_"] * len(palavra)
        letrasErradas = []
        print("Vamos começar, sua palavra tem  " + str(
            len(palavra)) + " letras.\n")
        for i in range(10):

            print("".join(tentativas))
            jogada = str(input("Digite uma letra: "))

            if jogada in palavra:

                for j in range(len(palavra)):
                    if palavra[j] == jogada:
                        tentativas[j] = jogada
                resposta = "".join(tentativas)

                print("Forca: " + resposta + " Chances restantes: " + str(
                    10 - i))

                if resposta == palavra:
                    print("Parabéns, você acertou a palavra é " + resposta + "!")
                    break
            else:
                letrasErradas += [jogada]
                resposta = ''.join(tentativas)
                print(f'Forca: {resposta} Chances restantes: {str(10 - i)}')
                letrasJaUsadas = ' '.join(letrasErradas)
                print(f'''A letra {jogada} não está na palavra
Letras erradas já digitadas: {letrasJaUsadas}''')
                if i < 0:
                    print("Você perdeu! Forca!")
                    break
        else:
            print("Você perdeu! Forca!")
            break
else:
    print('ADEUS!')
    exit()