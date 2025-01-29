# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
par = []
impar = []

while True:
   valor = int(input('Digite um número: '))
   lista.append(valor)
   if valor % 2 == 0:
      par.append(valor)
   else:
      impar.append(valor)
   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      print('Opção inválida. Tente novamente!')
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

par.sort()
impar.sort()

print(f'A lista copmleta é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')