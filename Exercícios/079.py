# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
   valor = int(input('Digite um valor: '))
   if valor in lista:
      print('Valor duplicado. Não vou adicionar na lista!')
   else:
      lista.append(valor)
   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      print('Opção inválida. Tente novamente!')
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break
print('-' * 40)
lista.sort()
print(f'Você digitou os valores {lista}')