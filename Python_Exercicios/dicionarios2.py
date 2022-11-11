jogos = {}
partidas = []

jogos['nome'] = str(input("Nome do jogador: "))
qtde = int(input("Quantidade de partidas: "))

for i in range(qtde):
    partidas.append(int(input(f"Quantidade de gols na {i+1}º partida: ")))

jogos['gols'] = partidas
jogos['total'] = sum(partidas)
print("=" * 50)
print(f"  O jogador {jogos['nome']} fez {jogos['total']} gols em {qtde} partidas!")
print("=" * 50)
for i, n in enumerate(jogos['gols']):
    print(f"  = Na partida {i+1} fez {n} gols.")
print(f"     com um total de {jogos['total']}.")