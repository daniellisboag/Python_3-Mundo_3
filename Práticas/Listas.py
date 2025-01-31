# Lista.
numeros = [2, 5, 9, 1]

# Adiciona valor 3 na posição 2.
numeros[2] = 3

# Acrescenta o valor 7 no começo da lista.
numeros.append(7)

# Coloca a lista em ordem reversa.
numeros.sort(reverse = True)

# Inserir na posição 2 o valor 0.
numeros.insert(2, 0)

# Remove o último elemento.
numeros.pop()

# Remove o o segundo elemento.
numeros.pop(2)

# Remove o valor 5 se estiver dentro da lista.
if 5 in numeros:
   numeros.remove(5)
else:
   print('Não achei o número 4')

print(numeros)

# Conta quantos elementos tem na lista.
print(f'Essa lista tem {len(numeros)} elementos.')

# Lista.
valores = []

# Adiciona valores a lista.
valores.append(5)
valores.append(9)
valores.append(4)

# Mostra a posição e os valores.
for c, v in enumerate(valores):
   print(f'Na posição {c} encontrei o valor {v}!')

valor = list()

# Adiciona na lista do valor 0 ao 5.
for c in range(0, 5):
   # Pergunta ao usuário qual valor será inserido na lista.
   valor.append(int(input('Digite um valor: ')))

# Enumera e mostra o valor da lista.
for c, v in enumerate(valor):
   print(f'Na posição {c} encontrei o valor {v}!')

# Lista
a = [2, 3, 4, 7]

# Lista 'b' interliga com a lista 'a'. Qualquer alteração na lista 'b' afeta a lista 'a'.
b = a

# Recebe os valores da lista 'a'.
b = a[:]

# Altera o segundo elemento da lista 'b'.
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Cria uma lista.
teste = list()

# Adiciona dados na lista.
teste.append('Daniel')
teste.append(24)

# Cria uma lista.
galera = list()

# Faz uma ligação da lista 'teste' para a lista 'galera'.
# galera.append(teste)

# Faz uma cópia da lista 'teste'.
galera.append(teste[:])

# Altera os dados da lista 'teste'.
teste[0] = 'Maria'
teste[1] = 22

# Faz mais uma cópia da lista 'teste'.
galera.append(teste[:])

print(galera)

# Cria uma lista dentro de outra lista.
galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

# Mostra a lista inteira.
print(galera)

# Mostra o elemento '0' da sublista '0'.
print(galera[0][0])

# Mostra o elemento '1' da sublista '2'. 
print(galera[2][1])

for p in galera:
   print(f'{p[0]} tem {p[1]} anos de idade.')
   print('-' * 30)

# Cria listas.
galera = []
dados = []

# Contador.
maior = menor = 0

for c in range(0, 3):
   dados.append(input('Nome: '))
   dados.append(int(input('Idade: ')))
   galera.append(dados[:])
   dados.clear()

print(galera)

for p in galera:
   if p[1] >= 21:
      print(f'{p[0]} é maior de idade.')
      maior += 1
   else:
      print(f'{p[0]} é menor de idade')
      menor += 1

print(f'Temos {maior} maiores e {menor} menores de idade.')