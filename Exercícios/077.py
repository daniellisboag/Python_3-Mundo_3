# Crie um programa que tenha uma tupla com várias palavras (não usar acentos.)
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'Futuro')

for c in palavras:
   print(f'\nNa palavra {c} temos ', end = '')
   for vogal in c:
      if vogal.upper() in 'AEIOU':
         print(vogal.upper(), end = ' ')