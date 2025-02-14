# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
   print(f'A área de um terreno {largura:.2f} x {comprimento:.2f} é de {largura * comprimento:.2f}m².')

print('Controle de área de terreno')
print('-' * 27)
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))