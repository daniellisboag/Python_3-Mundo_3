# Crie um programa que tenha uma tupla única com nomes de produtos e
# seus respctivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produto = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 40)
print('Listagem de preços'.center(40))
print('-' * 40)

for c in range(0, len(produto), 2):
   print(f'{produto[c]: <30}R$ {produto[c + 1]: >6.2f}')
print('-' * 40)