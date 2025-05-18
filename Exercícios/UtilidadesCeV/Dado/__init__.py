def leiaDinheiro(valor = 0):
   resultado = input(valor).strip().replace(',', '.')
   while True:
      if resultado.isalpha() or resultado == '':
         print(f'\033[0;31mErro! "{resultado}" é um valor inválido!\033[m')
         resultado = input('Digite um valor: R$').strip().replace(',', '.')
      else:
         return float(resultado)