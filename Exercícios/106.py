# Faça um mini-sistema que utiliza o interactive help do python. O usuário vai digitar o comando
# e o manual vai aparecere. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Observação: Use cores.

from time import sleep

cores = ('\033[m',        # 0 - Sem cor
         '\033[0;30;41m', # 1 - Vermelho
         '\033[0;30;42m', # 2 - Verde
         '\033[0;30;43m', # 3 - Amarelo
         '\033[0;30;44m', # 4 - Azul
         '\033[0;30;45m', # 5 - Roxo
         '\033[7;30m')    # 6 - Branco

def ajuda(com):
   titulo(f'Acessando o manual do comando \'{com}\'', 4)
   print(cores[6], end = '')
   help(com)
   print(cores[0], end = '')
   sleep(2)

comando = ''

def titulo(msg, cor = 0):
   tam = len(msg) + 4
   print(cores[cor], end = '')
   print('~' * tam)
   print(f'  {msg}')
   print('~' * tam)
   print(cores[0], end = '')
   sleep(1)

while True:
   titulo('Sistema de ajuda PyHelp', 2)
   comando = input('Função ou biblioteca> ')
   if comando.upper() == 'FIM':
      break
   else:
      ajuda(comando)
titulo('Até logo!', 1)