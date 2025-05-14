# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornadno um valor literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatório nas eleições.

def voto(ano):
   from datetime import date
   idade = date.today().year - ano
   if idade in (16, 17) or idade > 70:
      return f'Com {idade} anos: Voto opcional.'
   elif 17 < idade <= 70:
      return f'Com {idade} anos: Voto obrigatório.'
   else:
      return f'Com {idade} anos: Não vota.'

print(voto(int(input('Em que ano você nasceu? '))))