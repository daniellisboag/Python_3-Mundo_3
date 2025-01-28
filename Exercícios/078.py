# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
maior = []
menor = []

for c in range(0, 5):
   lista.append(int(input(f'Digite um valor para a posição {c}: ')))

for c, i in enumerate(lista):
   if max(lista) == i:
      maior.append(c)
   if min(lista) == i:
      menor.append(c)

print('-' * 40)
print(f'Você digitou os valores {max(lista)} nas posições {maior}')
print(f'Você digitou os valores {min(lista)} nas posições {menor}')