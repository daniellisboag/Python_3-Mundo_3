# Faça um programa que tenha uma função chamada contador(), que receba três parâmetro: início, fim
# e passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) uma contagem personalizada.

from time import sleep

def contagem(inicio, fim, passo):
   if passo < 0:
      passo = abs(passo)
   elif passo == 0:
      passo = 1
   print('-' * 35)
   print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
   if inicio < fim:
      for c in range(inicio, fim + 1, passo):
         print(c, end = ' ')
         sleep(0.2)
   else:
      for c in range(inicio, fim - 1, -passo):
         print(c, end = ' ')
         sleep(0.2)
   print('Fim!')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('-' * 35)
print('Agora é sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))