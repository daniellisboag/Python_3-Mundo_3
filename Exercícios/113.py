# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidadeda digitação de
# um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leia_int(valor):
   while True:
      try:
         resultado = int(input(valor))
      except (ValueError, TypeError):
         print('\033[0;031mErro! Digite um número inteiro válido.\033[m')
         continue
      except (KeyboardInterrupt):
         print('\033[0;031mEntrada de dados interrompida pelo usuário.\033[m')
         return 0
      else:
         return resultado

def leia_float(valor):
   while True:
      try:
         resultado = float(input(valor))
      except (ValueError, TypeError):
         print('\033[0;031mErro! Digite um número inteiro válido.\033[m')
         continue
      except (KeyboardInterrupt):
         print('\033[0;031mEntrada de dados interrompida pelo usuário.\033[m')
         return 0
      else:
         return resultado

inteiro = leia_int('Digite um número inteiro: ')
real = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')