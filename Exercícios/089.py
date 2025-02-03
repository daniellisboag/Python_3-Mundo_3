# Crie um programa que leia nome e duas notas de vários alunos e guarde
# tudo em uma lista composta. No final, mostre um boletim de cada um e
# permita que o usuário possa mostrar as notas de cada aluno individualmente.

lista = []
aluno = []
id = 0

while True:
   aluno.append(id)
   aluno.append(input('Nome: '))
   aluno.append(float(input('Nota 1: ')))
   aluno.append(float(input('Nota 2: ')))
   id += 1
   lista.append(aluno[:])
   aluno.clear()
   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      if opcao != 'S':
         print('Opção inválida. Tente novamente!')
         opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

print('-=' * 20)
print('N°   Nome           Média')
print('-' * 30)

for c in lista:
   print(f'{c[0]:<5}{c[1]:<15}{((c[2] + c[3]) / 2):>5.1f}')

media = 0

while media != 999:
   media = int(input('Digite o número do aluno para mostrar as notas (999 interrompe): '))
   for c in lista:
      if media == c[0]:
         print(f'As notas de {c[1]} são {c[2]}, {c[3]}')