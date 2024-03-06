from random import choice
from time import sleep
from sys import platform
from os import system

# Verificar a inatalação do modulo de cores
try:
    from termcolor import colored
except ModuleNotFoundError:
    if platform == 'linux':
        system('clear')
        print('Instalando módulo de cores...')
        system('pip install termcolor > /dev/null 2>&1')
        print('\nVerificando instalação...        ', end='', flush=True)

    elif platform == 'win32':
        system('cls')
        print('Instalando módulo de cores...')
        system('pip install termcolor')
        print('\nVerificando a instalação...        ',end='', flush=True)
        sleep(3)
    try:
        from termcolor import colored
        print('Done')
        sleep(1)
    except ModuleNotFoundError:
        print('Error ao instalar')
        sleep(1)
        exit()


def letrero(v: str):
    print(colored('=-', 'blue')*20)
    print(colored(f'{v}'.center(40), 'green'))
    print(colored('=-', 'blue')*20)


# Verificar a opção inicial
def verificar_opção():
    while True:
        system('clear||cls')
        letrero('JOGO DA VELHA')
        print('''[1] Jogar 1 v 1
[2] jogar contra IA (OFF)
[3] Jogar IA contra IA (OFF)
''')
        try:
            valor = int(input('Sua opção: '))
            if not 1<= valor <=3:
                print(colored('Somente números entre 1 e 3!', 'yellow'))
                sleep(1.5)
                system('clear||cls')
                continue
        except (ValueError, TypeError):
            print(colored('Digite um número inteiro válido!', 'red'))
            sleep(1.5)
            system('clear||cls')
        except KeyboardInterrupt:
            print('Saindo...')
            sleep(1.5)
            exit()

        else:
            return valor


# Menu com o gráfico do tabuleiro e os resultados
def menu(v1='',v2='',v3='',v4='',v5='',v6='',v7='',v8='',v9=''):

    print(colored('=-'*20, 'blue'))
    print(f'''
     |     |     
 {v1:^3} | {v2:^3} |{v3:^5}
_____|_____|_____
     |     |     
 {v4:^3} | {v5:^3} |{v6:^5}
_____|_____|_____
     |     |     
 {v7:^3} | {v8:^3} |{v9:^5}
     |     |     
''')
    print(colored('=-'*20, 'blue'))


def verificar_valor(msg:str):
    while True:
        try:
            pos = int(input(msg))
        
        except KeyboardInterrupt:
            print('\nSaindo do jogo...')
            sleep(2)
            exit()

        except (TypeError, ValueError,):
            print(colored('Digite um número inteiro válido!', 'red'))
            sleep(1)

            continue
        try:
            if 1<= pos <= 9:
                return pos
        except UnboundLocalError:
            continue
        
        else:
            print(colored('Somente números entre 1 e 9!', 'red'))
            sleep(1)


def verificar_vencedor(*tbl):
    # Verificar todas as linhas
    for linha in range(3):
        if all(posicao == jogador for posicao in tabuleiro[linha*3:linha*3+3]):
            return True
    # Verifica todas as colunas
    for coluna in range(3):
        if tabuleiro[coluna] == jogador and tabuleiro[coluna + 3] == jogador and tabuleiro[coluna + 6] == jogador:
            return True
    # Verifica as 2 diafonais
    if tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador:
        return True
    if tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador:
        return True
    
    if all(tbl):
        system('clear||cls')
        print(colored('=-'*20, 'blue'))
        print(colored(f'EMPATE!'.center(40), 'green'))
        menu(*tabuleiro)
        exit()



# Código principal
tabuleiro = ["", "", "", "", "", "", "", "", ""] # Armazenar o valor da jogada aqui.
placar_X = placar_O = 0
jogador = choice(['X', 'O'])
opção = verificar_opção()
if opção == 1:
    system('clear||cls')
    print('Formatando o cell....')
    sleep(5)
    print('É brincadeira amoor ksksksksk')
    sleep(5)
    system('clear||cls')

    
    letrero('JOGO DA VELHA')

    print('''1) Jogador "X" ou "O" Será aleatório.\n
2) Se caso vier "X" e você for querer 
ser o "O", então você será o jogador 2''')

    while True:
        menu(*tabuleiro)

        pos = verificar_valor(f'Jogador {jogador}, qual possição entre 1 e 9: ')

        if tabuleiro[pos-1] == '':
            tabuleiro[pos-1] = jogador
        else:
            print(colored(f'Este campo já está ocupado com o valor "{tabuleiro[pos-1]}"', 'yellow'))
            sleep(2)
        # Verficar Vencedor e verificar empate
        if verificar_vencedor(*tabuleiro):
            system('clear||cls')
            print(colored('=-'*20, 'blue'))
            print(colored(f'Jogador {jogador} VENCEU!'.center(40), 'green'))
            menu(*tabuleiro)

            break

        jogador = 'O' if jogador == 'X' else 'X'
        system('clear||cls')

elif opção == 2 or opção == 3:
    print('\nEssa opção ainda está em desenvolvimento...')
