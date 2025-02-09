# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de
# cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Média de idade do grupo.
# c) Uma lista com todas as mulheres.
# d) Uma lista com todas as pessoas com idade acima da média.

pessoas = []

while True:
   dados = {}
   nome = input('Nome: ')
   sexo = input('Sexo: [M/F]: ').strip().upper()[0]

   while sexo not in 'MF':
      print('Erro. Por favor, responda apenas M ou F.')
      sexo = input('Sexo: [M/F]: ').strip().upper()[0]
   idade = int(input('Idade: '))

   dados['Nome'] = nome
   dados['Sexo'] = sexo
   dados['Idade'] = idade
   pessoas.append(dados)

   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      print('Erro. Por favor, responda apenas S ou N.')
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

print('-=' * 20)
print(f'a) Ao todo temos pessoas {len(pessoas)} cadastradas.')

media = 0
for c in pessoas:
   media += c['Idade']

print(f'b) A média de idade é de {media / len(pessoas):.2f} anos.')

print(f'c) As mulheres cadastradas foram: ', end = '')
for c in pessoas:
   if c['Sexo'] in 'Ff':
      print(c['Nome'], end = ' ')

print('\nc) Lista das pessoas que estão com idade acima da média: ')
for c in pessoas:
   if c['Idade'] >= (media / len(pessoas)):
      print(f'Nome: {c['Nome']}; sexo: {c['Sexo']}; idade: {c['Idade']}')