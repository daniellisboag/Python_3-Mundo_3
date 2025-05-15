# Crie um programa que tenha a função leia_int(), que vai funcionar de forma semelhante à função input() do python, só que
# fazendo a validação para aceitar apenas um valor numérico.
# Exemplo: n = leia_int('Digite um número')

def leia_int(msg):
   situacao = False
   valor = 0
   while True:
      n = str(input(msg))
      if n.isnumeric():
         valor = int(n)
         situacao = True
      else:
         print('\033[0;031mErro! Digite um número inteiro válido.\033[m')
      if situacao:
         break
   return valor

n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')