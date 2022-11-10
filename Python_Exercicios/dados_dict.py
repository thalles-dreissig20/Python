from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador1': randint(1, 10),
        'jogador2': randint(1, 10),
        'jogador3': randint(1, 10),
        'jogador4': randint(1, 10),
        'jogador5': randint(1, 10)}

ranking = {}
for k, v in jogo.items():
    print(f"{k} tirou {v}.")
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("="*30)
print("==Ranking==")

for k, v in enumerate(ranking):
    print(f"{k+1}º lugar: {v[0]} tirando {v[1]}.")
    sleep(1)
