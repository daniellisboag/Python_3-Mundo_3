# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
# cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente
# de zero, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

dados = {}

dados['Nome'] = input('Nome: ')
nascimento = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - nascimento
dados['Carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['Carteira de trabalho'] != 0:
   dados['Ano de contratação'] = int(input('Ano de contratação: '))
   dados['Salário'] = int(input('Salário: R$'))
   dados['Aposentadoria'] = f'{35 + (dados['Ano de contratação'] - nascimento)} anos de idade'

print('-=' * 20)

for k, v in dados.items():
   print(f'{k}: {v}')