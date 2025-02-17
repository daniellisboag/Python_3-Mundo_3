# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro de lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.

from time import sleep
from random import randint

numeros = []

def sorteia():
   print('Sorteando 5 valores da lista: ', end = '')
   for c in range(0, 5):
      sleep(0.3)
      valor = randint(1, 10)
      numeros.append(valor)
      print(f'{valor}', end = ' ')
   print('Fim!')

def somaPar():
   par = 0
   for c in numeros:
      if c % 2 == 0:
         par += c
   print(f'Somando os valores pares de {numeros}, temos {par}')

sorteia()
somaPar()