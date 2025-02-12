# Aprimore o desafio 093 para que ele funciona com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
dados = []
gols = []
id = 0

while True:
   dados.append(input('Nome do jogador: '))
   dados.append(int(input(f'Quantas partidas {dados[0]} jogou? ')))
   for c in range(0, dados[1]):
      gols.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
   dados.append(gols[:])
   jogador[id] = dados[:]
   id += 1
   dados.clear()
   gols.clear()

   opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   while opcao not in 'SN':
      print('Opção inválida. Tente novamente!')
      opcao = input('Quer continuar? [S/N] ').strip().upper()[0]
   if opcao == 'N':
      break

print('-=' * 30)
print('Id   Nome              Gols              Total')
print('-' * 49)

for k, v in jogador.items():
   print(f'{k:<5}{v[0]:<18}{str(v[2]):<18}{sum(v[2]):<5}')

while True:
   dados_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
   for key in jogador.keys():
      if dados_jogador > key:
         print(f'Erro. Não existe jogador com id {dados_jogador}!')
   for k, v in jogador.items():
      if k == dados_jogador:
         print('-' * 49)
         print(f'Levantamento do jogador {v[0]}:')
         for c in range(0, v[1]):
            print(f'No jogo {c + 1} fez: {v[2][c]} gol(s).')
   print('-' * 49)
   if dados_jogador == 999:
      break