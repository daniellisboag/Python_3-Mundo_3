# Crie uma tupla preenchia com os 20 primeiros colocados da tabela do campeonato
# brasileiro de futebol, na ordem de colocação. Depois mostre:
# a) Apenas os 5 primeiros colocados.
# b) Os últimos 4 colocados da tabela.
# c) Uma lista com todos os times em ordem alfabética.
# d) Em que posição na tabela está o time da Chapecoense.

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético - PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético - GO')

print('-' * 40)
print(f'Lista de times do brasileirão: {times}')
print('-' * 40)
print(f'Os 5 primeiros são {times[0:5]}')
print('-' * 40)
print(f'Os 4 últimos são {times[-4:]}')
print('-' * 40)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-' * 40)
print(f'O Chapecoense está na {times.index('Chapecoense') + 1}° posição.')