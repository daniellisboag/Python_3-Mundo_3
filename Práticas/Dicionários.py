filme = {'titulo' : 'Star Wars', 'Ano' : 1977, 'Diretor' : 'George Lucas'}

print(filme.values())
print(filme.keys())
print(filme.items())

for k, v in filme.items():
   print(f'O {k} é {v}')