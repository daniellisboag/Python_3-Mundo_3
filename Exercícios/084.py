# Faça um programa que leia nome e pesoa de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) Quantas pessoas foram cadastradas.
# b) Uma listagem com as pessoas mais pesadas.
# c) Uma listagem com as pessoas mais leves.

pessoas = []
lista_maior = []
lista_menor = []
total_pessoas = peso_maior = 0

while True:
   dados = [input('Nome: '), float(input('Peso: '))]
   pessoas.append(dados)

   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      if opcao != 'S':
         print('Opção inválida. Tente novamente!')
         opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

for c in pessoas:
   if c[1] > peso_maior:
      peso_maior = c[1]
   peso_menor = peso_maior
   if c[1] < peso_menor:
      peso_menor = c[1]
   total_pessoas += 1

for i in pessoas:
   if i[1] == peso_maior:
      lista_maior.append(i[0])
   if i[1] == peso_menor:
      lista_menor.append(i[0])

print(f'Ao todo você cadastrou {total_pessoas} pessoas.')
print(f'O maior peso foi de {peso_maior:.1f}Kg. Peso de {lista_maior}')
print(f'O menor peso foi de {peso_menor:.1f}Kg. Peso de {lista_menor}')