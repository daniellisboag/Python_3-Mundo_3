# Cria um dicionário.
filme = {'titulo' : 'Star Wars', 'Ano' : 1977, 'Diretor' : 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
   print(f'O {k} é {v}')

# ---------------------------------------------------------

# Cria um dicionário.
pessoas = {'nome' : 'Daniel', 'sexo' : 'M', 'idade': 24}

print(pessoas['nome'])
print(f'O {pessoas['nome']} tem {pessoas['idade']} anos.')

# Mostra as chaves.
print(pessoas.keys())

# Mostra os valores.
print(pessoas.values())

# Mostra os itens.
print(pessoas.items())

# Apaga elemento 'sexo'.
del pessoas['sexo']

# Modifica o elemento 'nome'.
pessoas['nome'] = 'Gustavo'

# Adiciona um elemento ao dicionário
pessoas['peso'] = 65.5

for keys, values in pessoas.items():
   print(f'{keys} = {values}')

# ---------------------------------------------------------

# Cria uma lista
brasil = []

# Cria dois dicionários
estado_1 = {'uf' : 'Rio de Janeiro', 'sigla' : 'RJ'}
estado_2 = {'uf' : 'São Paulo', 'sigla' : 'SP'}

# Adiciona os dois dicionários na lista
brasil.append(estado_1)
brasil.append(estado_2)

# Mostra o elemento 'uf' do primeiro dicionário na lista.
print(brasil[0]['uf'])

# ---------------------------------------------------------

# Cria um dicionário.
estado = {}

# Cria uma lista.
brasil = []

for c in range (0, 3):

   # Adiciona valores ao dicionário.
   estado['uf'] = input('Unidade federativa: ')
   estado['sigla'] = input('Sigla do estado: ')

   # Faz uma cópia do dicionário para dentro da lista.
   brasil.append(estado.copy())

for i in brasil:
   for v in i.values():
      print(v, end = ' ')
   print()