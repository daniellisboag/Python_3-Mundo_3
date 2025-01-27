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