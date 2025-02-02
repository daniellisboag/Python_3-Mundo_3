# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
# jogo, cadastrando tudo em uma lista composta.

from time import sleep
from random import randint

print('-' * 30)
print(f'{'Jogo da mega sena':^30}')
print('-' * 30)

jogo = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'----- Sorteando {jogo} jogos -----')

lista = []

for c in range(0, jogo):
   sortear = []
   while len(sortear) < 6:
      numero = randint(1, 60)
      if numero not in sortear:
         sortear.append(numero)
   lista.append(sortear)
   lista[c].sort()
   sleep(0.3)
   print(f'Jogo {c + 1}: {lista[c]}')