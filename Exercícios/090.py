# Faça um programa que leia o nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = {}

dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f'Média do aluno {dados['Nome']}: '))

if dados['Média'] >= 7:
   dados['Situação'] = 'aprovado'
elif dados['Média'] <= 5 < 7:
   dados['Situação'] = 'recuperação'
else:
   dados['Situação'] = 'reprovado'

print('-=' * 20)

for k, v in dados.items():
   print(f'{k} do aluno: {v}')