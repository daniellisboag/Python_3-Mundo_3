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

def linha(tam = 42):
   return '-' * tam

def cabeçalho(texto):
   print(linha())
   print(texto.center(42))
   print(linha())

def menu(lista):
   cabeçalho('Menu principal')
   c = 1
   for item in lista:
      print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
      c += 1
   print(linha())
   opção = leia_int('\033[32mSua opção: \033[m')
   return opção