from random import choice
from time import sleep
from sys import platform
from os import system

# Verificar a inatalação do modulo de cores
try:
    from termcolor import colored
except ModuleNotFoundError:
    if platform.capitalize() == 'Linux':
        system('clear')
        print('Instalando módulo de cores...')
        system('pip install termcolor > /dev/null 2>&1')
        print('\nVerificando instalação...        ', end='', flush=True)

    elif platform.capitalize() == 'Win32':
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


# Função que mostra qualquer letra centralizada
def letrero(v: str):
    print(colored('=-', 'blue')*20)
    print(colored(f'{v}'.center(40), 'green'))
    print(colored('=-', 'blue')*20)


# Função que verifica a opção inicial
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


# Função que verifica o valor entre 1 e 9
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


# Função que vai verificar se há vencedor
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


# Função que verifica qual letra o jogador vai começar
def verficar_qual_cmç():
    while True:
        print(colored('-='*20, 'blue'))
        try:
            jogador = str(input('Quer ser "X" ou "O": ')).upper().strip()
            if jogador not in 'XO':
                print(colored('Error, digite um valor válido!', 'red'))
                sleep(1.5)
            elif jogador == '':
                print(colored('Campo obrigatório!', 'yellow'))
                sleep(1)
            else:
                return jogador
        except KeyboardInterrupt:
            print('Saindo do jogo...')
            sleep(1)
            exit()


#Função que verifica se o jogador quer continuar o jogo
def verificar_continuar():
    while True:
        try:
            continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
            if continuar not in 'SN':
                print(colored('Digite um valor válido!', 'red'))
                sleep(1)
                print(colored('=-'*20, 'blue'))
            elif continuar == 'N':
                print('Encerrando o Jodo...')
                sleep(2)
                exit()
            elif continuar == 'S':
                break
        except KeyboardInterrupt:
            print('Saindo do jogo...')
            exit()
        except IndexError:
            print(colored('Este campo é obrigatório!', 'light_yellow'))


# Função para limpar o tabuleiro
def limpar_tbl(*t: list):
    for i, tabu in enumerate(tabuleiro):
        tabuleiro[i] = ''



# Código principal
tabuleiro = ["", "", "", "", "", "", "", "", ""] # Armazenar o valor da jogada aqui.
placar_X = placar_O = 0

while True:
    opção = verificar_opção()
    if opção == 1: # Jogando contra outro jogador
        jogador = verficar_qual_cmç()
        system('clear||cls')
        letrero('JOGO DA VELHA')

        print('''1) Como jogar: O jogo da velha é composto
por 9 quadradinho, se voçê quiser jogar no meio, 
a posição do meio é o número 5. Espero que 
tenha entendido :)''')

        while True:
            menu(*tabuleiro)

            pos = verificar_valor(f'Jogador {jogador}, qual possição entre 1 e 9: ')

            if tabuleiro[pos-1] == '':
                tabuleiro[pos-1] = jogador
            else:
                print(colored(f'Este campo já está ocupado com o valor "{tabuleiro[pos-1]}"', 'yellow'))
                sleep(2)

            # Verficar Vencedor
            if verificar_vencedor(*tabuleiro):
                system('clear||cls')
                print(colored('=-'*20, 'blue'))
                print(colored(f'Jogador {jogador} VENCEU!'.center(40), 'green'))
                menu(*tabuleiro)

                # Contador de placar
                if jogador == 'X':
                    placar_X += 1
                else:
                    placar_O += 1

                # Mostrar o placar
                print(colored('PLACAR'.center(40),'green'))
                print(colored(f'Jogador X: {placar_X} vs {placar_O} :Jogador O'.center(40), 'light_magenta'))
                print(colored('=-'*20, 'blue'))
                # Limpar o tabuleiro
                limpar_tbl(*tabuleiro)
                # Chamar função para verificar se quer continuar
                verificar_continuar()
            
             # Verificar empate
            if all(tabuleiro):
                system('clear||cls')
                print(colored('=-'*20, 'blue'))
                print(colored(f'EMPATE!'.center(40), 'green'))
                menu(*tabuleiro)
                # Mostrando o placar
                print(colored('PLACAR'.center(40),'green'))
                print(colored(f'Jogador X: {placar_X} vs {placar_O} :Jogador O'.center(40), 'light_magenta'))
                print(colored('=-'*20, 'blue'))
                limpar_tbl(*tabuleiro) # Limpar o tabuleiro
                verificar_continuar()


            jogador = 'O' if jogador == 'X' else 'X'
            system('clear||cls')

    elif opção == 2 or opção == 3:
        print('\nEssa opção ainda está em desenvolvimento...')
        sleep(2.3)
