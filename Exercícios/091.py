# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
# ordem, sabendo que o vencedor tirou o maior número no dado.

from time import sleep
from random import randint
from operator import itemgetter

dados = {}
ranking = []

for c in range(1, 5):
   dados[f'Jogador {c}'] = randint(1, 6)

for k, v in dados.items():
   print(f'{k} tirou {v} no dado.')
   sleep(0.4)

ranking = sorted(dados.items(), key = itemgetter(1), reverse = True)

print('-=' * 20)
print('Ranking dos jogadores')

for i, v in enumerate(ranking):
   print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
   sleep(0.4)