# Modifique as funções que foram criadas no desafio 107 para que elas aceitem
# um parâmetro a mais, informando se o valor retornado por elas vai ser ou
# não formatado pela função moeda(), desenvolvida no desafio 108.

from moeda import aumentar, dobro, metade, moeda, diminuir

valor = float(input('Digite um valor: R$'))
print(f'A metade de {moeda(valor)} é {metade(valor, True)}')
print(f'O dobro de {moeda(valor)} é {dobro(valor, True)}')
print(f'Aumentando 10%, temos {aumentar(valor, 10, True)}')
print(f'Reduzindo 13%, temos {diminuir(valor, 13, True)}')