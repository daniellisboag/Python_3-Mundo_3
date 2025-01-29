# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

lista = []
opcao = ' '

while True:
   lista.append(int(input('Digite um valor: ')))
   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      print('Opção inválida. Tente novamente!')
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

lista.sort(reverse = True)

print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')

if 5 in lista:
   print(f'O valor 5 faz parte da lista!')
else:
   print('O valor 5 não faz parte da lista!')