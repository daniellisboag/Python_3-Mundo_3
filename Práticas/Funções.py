def mensagem(msg):
   print('-' * 30)
   print(msg)
   print('-' * 30)

mensagem(f'{'Curso em vídeo':^30}')
mensagem(f'{'Aprenda python':^30}')
mensagem(f'{'Daniel Lisboa':^30}')

# -----------------------------------------------------------------------

def soma(a, b):
   soma = a + b
   print(f'A = {a} e B = {b}')
   print(f'A soma de A + B = {soma}')

soma(4, 5)
soma(a = 8, b = 9)
soma(b = 2, a = 1)

# -----------------------------------------------------------------------

def contador(*num):
   for c in num:
      print(c, end = ' ')
   print()

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# -----------------------------------------------------------------------

def contador(*num):
   print(f'Recebi os valores {num} e são ao todo {len(num)} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# -----------------------------------------------------------------------

def dobra(lst):
   posicao = 0
   while posicao < len(lst):
      lst[posicao] *= 2
      posicao += 1

valores = [6, 3, 9, 1, 0, 2]

print(valores)
dobra(valores)
print(valores)

# -----------------------------------------------------------------------

def soma(*valores):
   s = 0
   for c in valores:
      s += c
   print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)