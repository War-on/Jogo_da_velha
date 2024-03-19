
#############################################################
#######                 JODO DA VELHA                 #######
#######            CREATED BY leomoreiraYT            #######
#######   insta: https://instagram.com/leomoreirayt   #######
#############################################################

from random import choice
from time import sleep
import sys
from os import system
from datetime import datetime

# Verificar a inatalação do modulo de cores
hora = datetime.today().hour # Pegando a hora
try:
    from termcolor import colored
except ModuleNotFoundError:
    if sys.platform.capitalize() == 'Linux':
        system('clear')
        print('Instalando módulo de cores...')
        system('pip install termcolor > /dev/null 2>&1')
        print('\nVerificando instalação...        ', end='', flush=True)

    elif sys.platform.capitalize() == 'Win32':
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


def animacao_pensando():
    mensagem = "Pensando"
    for c in range(5):
        for i in range(4):
            sys.stdout.write(f"\r{mensagem}{'.' * i}   ")
            sys.stdout.flush()
            sleep(0.1)


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
        print('''[1] Jogar 1 v 1         (\033[32mON\033[m)
[2] jogar contra IA     (\033[32mON\033[m)
[3] Jogar IA contra IA  (\033[31mOFF\033[m)
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
def verficar_qual_cmç(nome):
    while True:
        print(colored('-='*20, 'blue'))
        try:
            jogador = str(input(f'{nome}, quer ser "X" ou "O": ')).upper().strip()
            if jogador not in 'XO':
                print(colored('Digite um valor válido!', 'red'))
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


# Função que mostrará o placar dos jogadores
def placar(nome1, placar_X, placar_O, nome2):
        print(colored('PLACAR'.center(40),'green'))
        print(colored(f'{nome1} \'{placar_X}\' vs \'{placar_O}\' {nome2}'.center(40), 'light_magenta'))
        print(colored('=-'*20, 'blue'))


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
            sleep(.5)


# Função para limpar o tabuleiro
def limpar_tbl(*t: list):
    for i, tabu in enumerate(t):
        tabuleiro[i] = ''


def limpar():
    system('clear||cls')


def ler_nome_Jogagores(ler_jogador=False ,ia=False):
    # Ler nome dos 2 jogadores
    if ler_jogador:
        coint = 1
        jogadores = ['Jogador 1', 'Jogador 2']
        while True:
            try:
                print(colored('=-'*20, 'blue'))
                nome_jogador = str(input(f'Jogador {coint}, Qual seu nome: ')).capitalize().strip()
                if nome_jogador == '':
                    print(colored('Campo obrigatório!', 'yellow'))
                    sleep(1)
                    continue
                elif nome_jogador.isnumeric():
                    print(colored('Número não é nome!', 'yellow'))
                    sleep(1)
                    continue
                elif len(nome_jogador) <3:
                    print(colored('Digite um nome que tenha mais de 2 caracteres!', 'yellow'))
                    sleep(1)
                    continue
            except KeyboardInterrupt:
                print('Saindo do jogo...')
                sleep(2)
                exit()
            else:
                if coint == 1:
                    coint += 1
                    jogadores[0] = nome_jogador
                    continue
                elif coint == 2:
                    jogadores[1] = nome_jogador
                    return jogadores

    if ia:
        while True:
            try:
                print(colored('=-'*20, 'blue'))
                nome_jogador = str(input('Qual seu nome: ')).capitalize().strip()
                if nome_jogador == '':
                    print(colored('Campo obrigatório!', 'yellow'))
                    sleep(1)
                    continue
                elif nome_jogador.isnumeric():
                    print(colored('Número não é nome!', 'yellow'))
                    sleep(1)
                    continue
                elif len(nome_jogador) <3:
                    print(colored('Digite um nome que tenha mais de 2 caracteres!', 'yellow'))
                    sleep(1)
                    continue
            except KeyboardInterrupt:
                print('Saindo do jogo...')
                sleep(2)
                exit()
            else:
                return nome_jogador


def placar_nome(nome='', nomeT=False, empateT=False):
    if nomeT:
        system('clear||cls')
        print(colored('=-'*20, 'blue'))
        print(colored(f'Jogador {nome} VENCEU!'.center(40), 'green'))
        menu(*tabuleiro)

    if empateT:
        system('clear||cls')
        print(colored('=-'*20, 'blue'))
        print(colored('EMPATE'.center(40), 'green'))
        menu(*tabuleiro)

# MINI MAX (JOGADA DA IA)
def jogada_IA(tabuleiro):
    melhor_pontuacao = float('-inf')
    melhor_jogada = None
    
    for i in range(9):
        if tabuleiro[i] == '':
            tabuleiro[i] = 'O'
            pontuacao = minimax(tabuleiro, 0, False)
            tabuleiro[i] = ''
            
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_jogada = i
                
    return melhor_jogada

def minimax(tabuleiro, profundidade, maximizando):
    resultado = verificar_resultado(tabuleiro)
    
    if resultado is not None:
        if resultado == 'O':
            return 10 - profundidade
        elif resultado == 'X':
            return -10 + profundidade
        else:
            return 0
    
    if maximizando:
        melhor_pontuacao = float('-inf')
        for i in range(9):
            if tabuleiro[i] == '':
                tabuleiro[i] = 'O'
                pontuacao = minimax(tabuleiro, profundidade + 1, False)
                tabuleiro[i] = ''
                melhor_pontuacao = max(pontuacao, melhor_pontuacao)
        return melhor_pontuacao
    else:
        melhor_pontuacao = float('inf')
        for i in range(9):
            if tabuleiro[i] == '':
                tabuleiro[i] = 'X'
                pontuacao = minimax(tabuleiro, profundidade + 1, True)
                tabuleiro[i] = ''
                melhor_pontuacao = min(pontuacao, melhor_pontuacao)
        return melhor_pontuacao


def verificar_resultado(tabuleiro):
    # Verificar todas as linhas
    for linha in range(3):
        if all(posicao == 'X' for posicao in tabuleiro[linha*3:linha*3+3]):
            return 'X'
        elif all(posicao == 'O' for posicao in tabuleiro[linha*3:linha*3+3]):
            return 'O'
    
    # Verificar todas as colunas
    for coluna in range(3):
        if tabuleiro[coluna] == 'X' and tabuleiro[coluna + 3] == 'X' and tabuleiro[coluna + 6] == 'X':
            return 'X'
        elif tabuleiro[coluna] == 'O' and tabuleiro[coluna + 3] == 'O' and tabuleiro[coluna + 6] == 'O':
            return 'O'
    
    # Verificar as duas diagonais
    if tabuleiro[0] == 'X' and tabuleiro[4] == 'X' and tabuleiro[8] == 'X':
        return 'X'
    elif tabuleiro[0] == 'O' and tabuleiro[4] == 'O' and tabuleiro[8] == 'O':
        return 'O'
    elif tabuleiro[2] == 'X' and tabuleiro[4] == 'X' and tabuleiro[6] == 'X':
        return 'X'
    elif tabuleiro[2] == 'O' and tabuleiro[4] == 'O' and tabuleiro[6] == 'O':
        return 'O'
    
    # Se não houver vencedor
    if '' not in tabuleiro:
        return 'Empate'
    
    # Se o jogo ainda estiver em andamento
    return None



# Código principal
tabuleiro = ["", "", "", "", "", "", "", "", ""] # Armazenar o valor da jogada aqui.
placar_X = placar_O = 0
coint = 0

# INÍCIO DO JOGO!
while True:
    opção = verificar_opção()
    if opção == 1: # Jogando 1 v 1
        # Ler os nomes dos jogadores
        X_OU_O = ['', '', 0]
        O_OU_X = ['', '', 0]
        jogadores = ler_nome_Jogagores(ler_jogador=True)
        X_OU_O[0] = jogadores[0] # Nome jogador 1
        O_OU_X[0] = jogadores[1] # Nome jogador 2
        jogador = verficar_qual_cmç(jogadores[0]) # Verificar se Jogador 1 vai ser X ou O
        X_OU_O[1] = jogador
        if jogador == 'X':
            O_OU_X[1] = 'O'
            print(colored(f'Certo! {jogadores[1]} ficará com "O".', 'green'))
            sleep(3.5)
        else:
            O_OU_X[1] = 'X'
            print(colored(f'Certo! {jogadores[1]} ficará com "X".', 'green'))
            sleep(3.5)
        system('clear||cls')
        letrero('JOGO DA VELHA')

        print('''1) Como jogar: O jogo da velha é composto
por 9 quadradinho, se voçê quiser jogar no meio, 
a posição do meio é o número 5. Espero que 
tenha entendido :)''')

        while True:
            menu(*tabuleiro)
            pos = verificar_valor(f'{jogadores[coint]} \'{jogador}\': Qual possição entre 1 e 9: ')

            if tabuleiro[pos-1] == '':
                tabuleiro[pos-1] = jogador
            else:
                print(colored(f'Este campo já está ocupado com o valor "{tabuleiro[pos-1]}"', 'yellow'))
                sleep(2)
                system('clear||cls')
                continue

            # Verficar Vencedor

            if verificar_vencedor(*tabuleiro):
                placar_nome(jogadores[coint], True)

                # Contador de placar
                if jogadores[coint] == X_OU_O[0]:
                    X_OU_O[2] += 1

                else:
                    O_OU_X[2] += 1

                

                # Mostrar o placar
                placar(X_OU_O[0], X_OU_O[2], O_OU_X[2], O_OU_X[0])

                # Limpar o tabuleiro
                limpar_tbl(*tabuleiro)

                # Chamar função para verificar se quer continuar
                verificar_continuar()

            # Verificar empate
            if all(tabuleiro):
                placar_nome(empateT=True)
                menu(*tabuleiro)
                placar(X_OU_O[0], X_OU_O[2], O_OU_X[2], O_OU_X[0])
                limpar_tbl(*tabuleiro)
                verificar_continuar()

            coint = 1 if coint == 0 else 0

            jogador = 'O' if jogador == 'X' else 'X'
            system('clear||cls')

    # JOGAR CONTRA IA
    elif opção == 2:
        print()
        nome_IA = 'Stil' # Nome da IA
        jogadores = ['<desconhecido>', nome_IA] # Guardando o nome dos 2 jogadores
        # Tratamento de frase
        if 6 <= hora < 12:
            comprimento = 'Bom dia!'
        elif 12 <= hora < 18:
            comprimento = 'Boa tarde!'
        elif 18 <= hora < 24:
            comprimento = 'Boa noite!'
        elif 0 <= hora < 6:
            comprimento = 'Boa madrugada'
        
        # Primeira fala da IA
        frase1 = f'IA: Oi, {comprimento} Me chamo {nome_IA} e eu irei jogar o jogo da velha com você.'

        for f in frase1:
            print(f, flush=True, end='')
            sleep(.03) 
        print()

        jogador = ler_nome_Jogagores(ia=True)
        jogadores[0] = jogador

        # Segunda fala da IA
        frase2 = f'\n{nome_IA}: Certo \'{jogador}\'. Você vai ser sempre o \'X\' e eu o \'O\', okay.'
        for f in frase2:
            print(f, end='', flush=True)
            sleep(0.03)
        print()
        sleep(3)

        # Terceira fala da IA
        frase3 = f'\n{nome_IA}: Seu desafio e tentar me vencer. Boa sorte :D.'
        for f in frase3:
            print(f, end='', flush=True)
            sleep(.03)
        print()
        sleep(5)

        system('clear||cls')


        # COMEÇANDO O JOGO
        jogador = 'X'
        placar_X = placar_O = 0
        while True:
            if verificar_resultado(tabuleiro) == 'X': # Vitória do jogador X
                limpar()
                placar_X += 1
                placar_nome(jogadores[0], True, False)
                placar(jogadores[0], placar_X, placar_O, jogadores[1])
                limpar_tbl(*tabuleiro)
                verificar_continuar()
                jogador = 'X'
                limpar()

            elif verificar_resultado(tabuleiro) == 'O': # Vitória do jogador O
                limpar()
                placar_O += 1
                placar_nome(nome_IA, True, False)
                placar(jogadores[0], placar_X, placar_O, jogadores[1])
                limpar_tbl(*tabuleiro)
                verificar_continuar()
                jogador = 'X'
                limpar()

            elif verificar_resultado(tabuleiro) == 'Empate': # Empate
                limpar()
                placar_nome(empateT=True)
                placar(jogadores[0], placar_X, placar_O, jogadores[1])
                limpar_tbl(*tabuleiro)
                verificar_continuar()
                jogador = 'X'
                limpar()

            # IA irá jogar
            if jogador == 'O':
                limpar()
                jogada = jogada_IA(tabuleiro)
                tabuleiro[jogada] = 'O'
                jogador = 'X'
                continue
            
            # Jogador irá jogar
            if jogador == 'X':
                while True:
                    menu(*tabuleiro)
                    pos = verificar_valor(f'{jogadores[0]} \'X\': Qual possição entre 1 e 9: ')
                    if tabuleiro[pos-1] == '':
                        tabuleiro[pos-1] = jogador
                        jogador = 'O'
                        break
                    else:
                        print(colored(f'Este campo já está ocupado com o valor "{tabuleiro[pos-1]}"', 'yellow'))
                        sleep(2)
                        system('clear||cls')
                        continue
            if verificar_resultado(tabuleiro) != 'Empate':
                system('clear||cls')
                menu(*tabuleiro)
                animacao_pensando()


    elif opção == 3:
        print('\nEssa opção ainda está em desenvolvimento...')
        sleep(2.3)
