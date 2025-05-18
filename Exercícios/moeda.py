def metade(valor = 0, formato = False):
   if formato == False:
      return valor / 2
   else:
      return moeda(valor / 2)

def aumentar(valor = 0, taxa = 0, formato = False):
   if formato == False:
      return valor + (valor * taxa / 100)
   else:
      return moeda(valor + (valor * taxa / 100))

def dobro(valor = 0, formato = False):
   if formato == False:
      return valor * 2
   else:
      return moeda(valor * 2)

def diminuir(valor = 0, taxa = 0, formato = False):
   if formato == False:
      return valor - (valor * taxa / 100)
   else:
      return moeda(valor - (valor * taxa / 100))

def moeda(valor = 0, moeda = 'R$'):
   return f'{moeda}{valor:.2f}'.replace('.', ',')

def resumo(valor = 0, aumento = 0, redução = 0):
   print('-' * 35)
   print('Resumo do valor'.center(35))
   print('-' * 35)
   print(f'Preço analisado: \t{moeda(valor)}')
   print(f'Dobro do preço: \t{dobro(valor, True)}')
   print(f'Metade do preço: \t{metade(valor, True)}')
   print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
   print(f'{redução}% de redução: \t{diminuir(valor, redução, True)}')
   print('-' * 35)