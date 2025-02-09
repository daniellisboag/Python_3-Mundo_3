# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
# ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols
# feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o
# total de gols feitos durante o campeonato.

dados = {}
gols = []

dados['Nome'] = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {dados['Nome']} jogou? '))

for c in range(0, partidas):
   gols.append(int(input(f'Quantos gols na {c + 1}° partida? ')))

dados['Gols'] = gols
dados['Total'] = sum(gols)

print('-=' * 20)
print(dados)
print('-=' * 20)

for k, v in dados.items():
   print(f'{k}: {v}')

print('-=' * 20)
print(f'O jogador {dados['Nome']} jogou {partidas} partidas.')

for c, i in enumerate(gols):
   print(f'Na {c + 1}° partida fez {i} gols.')
print(f'Total de gols: {dados['Total']}')