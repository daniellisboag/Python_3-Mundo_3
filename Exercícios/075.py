# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em
# uma tupla. No final, mostre:
# a) Quantas vezes apareceu o valor 9.
# b) Em que posição foi digitado o primeiro valor 3.
# c) Quais foram os números pares.

numeros = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 in numeros:
   print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição.')
else:
   print('O valor 3 não apareceu em nenhuma posição.')

print(f'Os valores pares digitados foram ', end = '')
for c in numeros:
   if c % 2 == 0:
      print(c, end = ' ')