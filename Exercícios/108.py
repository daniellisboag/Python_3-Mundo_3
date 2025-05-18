# Adapte o código do desafio 107, criando uma função adicional chamada
# moeda() que consiga mostrar os valores como um valor monetário formatado.

# Resolução do curso
import moeda

valor = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')

# Minha resolução
'''from moeda import aumentar, dobro, metade, moeda

valor = float(input('Digite um valor: R$'))
print(f'A metade de {moeda(valor)} é {moeda(metade(valor))}')
print(f'O dobro de {moeda(valor)} é {moeda(dobro(valor))}')
print(f'Aumentando 10%, temos {moeda(aumentar(valor, 10))}')'''