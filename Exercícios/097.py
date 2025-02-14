# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.
# Exemplo: escreva('Olá, Mundo!')
# Saída:
# ---------------------
#      Olá, mundo!     
# ---------------------

def mensagem(msg):
   print('-' * (len(msg) + 2))
   print(f'{msg:^{len(msg) + 2}}')
   print('-' * (len(msg) + 2))

mensagem('Daniel Lisboa')
mensagem('Curso de Python no YouTube')
mensagem('CeV')