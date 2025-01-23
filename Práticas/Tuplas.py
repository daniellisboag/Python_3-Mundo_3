# Tupla
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

# Hambúrguer, Suco, Pizza, Pudim, Batata frita
print(lanche)

# Pizza
print(lanche[2])

# Hambúrguer, Suco
print(lanche[0:2])

# Suco, Pizza, Pudim, Batata frita
print(lanche[1:])

# Batata frita
print(lanche[-1])

# Suco
print(lanche[-4])

# 5
print(len(lanche))

# Lanche -> range(0, 5)
for c in lanche:
   print(c)

# Ou
for i in range(0, len(lanche)):
   print(lanche[i])

# Mostrando a posição
for posicao, i in enumerate(lanche):
   print(posicao, i)

# sorted() classificado em ordem alfabética
print(sorted(lanche))

# ---------------------------------------------------------------

# Tupla
numero_1 = (2, 5, 4)
numero_2 = (5, 8, 1, 2)

# Faz a junção das tuplas e não a soma
print(numero_1 + numero_2)

# Conta quantas vezes o número 5 aparece
print((numero_1 + numero_2).count(9))

# Mostra em que posição está o número 2
print((numero_1 + numero_2).index(2))

# Mostra em que posição está o número 2 a partir da posição 1
print((numero_1 + numero_2).index(2, 1))

# ---------------------------------------------------------------

# Tupla
pessoa = ('Daniel', 24, 'M', 65.50)

# Daniel, 24, M, 65.50
print(pessoa)

# Apaga a variável
del(pessoa)

# Erro
print(pessoa)