# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
   contador = maiorr = 0
   print('-' * 50)
   print('Analisando os valores passados...')
   for c in num:
      contador += 1
      if c > maiorr:
         maiorr = c
      print(c, end = ' ')
      sleep(0.3)
   print(f'Foram informados {contador} valores ao todo.')
   print(f'O maior valor informado foi {maiorr}')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()