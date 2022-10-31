"""Faça um programa que ajude um jogador da MEGASENA a criar palpites. O programa 
vai perguntar quantos jogos serão sorteados e vai gerar 6 números entre 1 e 60 para 
cada jogo, cadastrando tudo em uma única lista composta. """

from random import randint
from time import sleep

palpites = []
print('=' * 35 + f'\n{"PALPITE MEGA SENA":^35}\n' + '=' * 35)

quantidade_Jogos = int(input('Quantos jogos deseja: '))
print(f'\n{" > SORTEANDO VALORES < ":~^35}')
print()

for contagem in range(quantidade_Jogos):
    jogo = []
    for qtdValores in range(6):
        sorteio = randint(1, 60)

        if sorteio in jogo:
            sorteio = randint(1, 60)
            jogo.append(sorteio)
        else:
            jogo.append(sorteio)

    jogo.sort()
    palpites.append(jogo[:])
    print(f'Jogo {contagem + 1}: {palpites[contagem]}')
    sleep(0.5)
print()
print(f'{" > BOA SORTE < ":~^35}')