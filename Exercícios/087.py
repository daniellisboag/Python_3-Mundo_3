# Aprimore o desafio anterior, mostrando no final:
# a) A soma de todos o valores pares digitados.
# b) A soma dos valores da terceira coluna.
# c) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira_coluna = segunda_linha = 0

for c in range(0, 3):
   for i in range(0, 3):
      matriz[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))
      if matriz[c][i] % 2 == 0:
         par += matriz[c][i]
      if i == 2:
         terceira_coluna += matriz[c][i]
      if c == 1:
         if matriz[c][i] > segunda_linha:
           segunda_linha = matriz[c][i]

print('-' * 30)

for c in range(0, 3):
   for i in range(0, 3):
      print(f'[{matriz[c][i]:^5}]', end = '')
   print()

print('-' * 30)

print(f'A soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}.')
print(f'O maior valor da segunda linha é {segunda_linha}.')