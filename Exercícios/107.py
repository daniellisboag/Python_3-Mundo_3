# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from moeda import aumentar, dobro, metade

valor = float(input('Digite um valor: R$'))
print(f'A metade de R${valor} é R${metade(valor)}')
print(f'O dobro de R${valor} é R${dobro(valor)}')
print(f'Aumentando 10%, temos R${aumentar(valor, 10)}')