# Define uma função que imprime uma mensagem.
def mensagem(msg):
   print('-' * 30)
   print(msg)
   print('-' * 30)

# Chamada da função com mensagens centralizadas.
mensagem(f'{'Curso em vídeo':^30}')
mensagem(f'{'Aprenda python':^30}')
mensagem(f'{'Daniel Lisboa':^30}')

# -----------------------------------------------------------------------

# Define uma função que soma dois valores e imprime o processo.
def soma(a, b):
   soma = a + b
   print(f'A = {a} e B = {b}')
   print(f'A soma de A + B = {soma}')

# Chamadas da função com e sem argumentos nomeados.
soma(4, 5)
soma(a = 8, b = 9)
soma(b = 2, a = 1)

# -----------------------------------------------------------------------

# Define uma função que recebe vários valores e imprime todos na mesma linha.
def contador(*num):
   for c in num:
      print(c, end = ' ')
   print()

# Chamadas da função com diferentes quantidades de argumentos.
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# -----------------------------------------------------------------------

# Define uma função que exibe os valores recebidos e a quantidade total.
def contador(*num):
   print(f'Recebi os valores {num} e são ao todo {len(num)} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

# -----------------------------------------------------------------------

# Função que dobra os valores de uma lista recebida como argumento.
def dobra(lst):
   posicao = 0
   while posicao < len(lst):
      lst[posicao] *= 2
      posicao += 1

valores = [6, 3, 9, 1, 0, 2]

# Antes da modificação.
print(valores)

# Dobra os valores da lista.
dobra(valores)

# Após a modificação.
print(valores)

# -----------------------------------------------------------------------

# Função que soma uma quantidade variável de valores.
def soma(*valores):
   s = 0
   for c in valores:
      s += c
   print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(2, 9, 4)

# -----------------------------------------------------------------------

# Exibe a documentação da função print.
help(print)

# Mostra a documentação do input diretamente.
print(input.__doc__)

# Exibe a ajuda da função input usando help().
help(input)

# -----------------------------------------------------------------------

# Função com docstring explicando o propósito e os parâmetros.
def contador(inicio, fim, passo):
   """
   -> Faz uma contagem e mostra na tela.
   :parâmetro inicio: início da contagem.
   :parâmetro fim: fim da contagem.
   :parâmetro passo: passo da contagem.
   :return: sem retorno.
   Função criada por Gustavo Guanabara do canal Curso em Vídeo.
   """
   c = inicio
   while c <= fim:
      print(f'{c}', end = '..')
      c += passo
   print('Fim!')

contador(2, 10, 2)

# Exibe a docstring da função 'contador'.
help(contador)

# -----------------------------------------------------------------------

# Função com valores padrão nos parâmetros.
def somar(a = 0, b = 0, c = 0):
   """
   -> Faz a soma de três valores e mostra o resultado na tela.
   :parâmetro a: o primeiro valor.
   :parâmetro b: o segundo valor.
   :parâmetro c: o terceiro valor.
   Função criada por Gustavo Guanabara do canal Curso em Vídeo.
   """
   s = a + b + c
   print(f'A soma vale {s}')


somar(3, 8)

# -----------------------------------------------------------------------

# Define uma função chamada teste().
def teste():
   x = 8 # Cria a variável local 'x' com valor 8 (só existe dentro da função).
   print(f'Na função teste, n vale {n}') # Acessa a variável global 'n', que vale 2.
   print(f'Na função teste, x vale {x}') # Acessa a variável local 'x'.

# Variável global 'n' criada no escopo principal do programa.
n = 2

# Mostra o valor da variável 'n' no escopo principal.
print(f'No programa principal, n vale {n}')

# Chama a função teste() que imprime os valores de 'n' (global) e 'x' (local).
teste()

# Tenta mostrar o valor de 'x' no escopo principal (isso vai gerar um erro!).
print(f'No programa principal, n vale {x}') # Erro! 'x' não existe aqui.

# -----------------------------------------------------------------------

# Define a função teste, que recebe um argumento b.
def teste(b):
   a = 8 # 'a' é uma variável local à função, ela existe apenas dentro da função.
   b += 4 # 'b' é passado como parâmetro para a função. O valor de b é incrementado em 4.
   c = 2 # Criação de uma variável local 'c' com valor 2, também só existe dentro da função.
   
   # Imprime o valor da variável 'a' dentro da função.
   print(f'A dentro vale {a}') # Vai imprimir 'A dentro vale 8', pois 'a' foi definida dentro da função teste.
   
   # Imprime o valor de 'b' após ser incrementado dentro da função.
   print(f'B dentro vale {b}') # Vai imprimir 'B dentro vale 9', pois 'b' foi incrementado em 4.
   
   # Imprime o valor de 'c' dentro da função.
   print(f'C dentro vale {c}') # Vai imprimir 'C dentro vale 2', pois 'c' foi definido localmente.

# Define a variável 'a' no programa principal.
a = 5

# Chama a função teste, passando o valor de 'a' como argumento para 'b'.
teste(a)

# Imprime o valor de 'a' no programa principal.
print(f'A fora vale {a}') # Vai imprimir 'A fora vale 5', pois 'a' no programa principal não foi alterada pela função.

# -----------------------------------------------------------------------

# Define a função teste, que recebe um argumento b.
def teste(b):
   global a # 'global' indica que estamos usando a variável 'a' que é global, ou seja, no escopo principal.
   a = 8 # Agora 'a' é alterada no escopo global (programa principal), não apenas dentro da função.
   b += 4 # 'b' é passado como argumento para a função e incrementado em 4. Isso não afeta a variável global 'a'.
   c = 2 # 'c' é uma variável local à função.

   # Imprime o valor de 'a' dentro da função (a variável global).
   print(f'A dentro vale {a}') # Vai imprimir 'A dentro vale 8', pois 'a' foi alterada globalmente.

   # Imprime o valor de 'b' dentro da função após o incremento.
   print(f'B dentro vale {b}') # Vai imprimir 'B dentro vale 9', porque 'b' foi incrementado dentro da função.

   # Imprime o valor de 'c' dentro da função.
   print(f'C dentro vale {c}') # Vai imprimir 'C dentro vale 2', já que 'c' é local à função.

# Define a variável global 'a' no programa principal.
a = 5

# Chama a função teste, passando o valor de 'a' como argumento para 'b'
teste(a)

# Imprime o valor de 'a' no programa principal após a execução da função.
print(f'A fora vale {a}') # Vai imprimir 'A fora vale 8', porque 'a' foi alterada globalmente pela função.

# -----------------------------------------------------------------------

# Define a função somar com três parâmetros opcionais, todos com valor padrão 0.
def somar(a = 0, b = 0, c = 0):
   s = a + b + c # Soma os três valores recebidos como argumento.
   return s # Retorna o resultado da soma para quem chamou a função.

resposta_1 = somar(3, 2, 5) # Passa os três valores: a = 3, b = 2, c = 5 → soma = 10
resposta_2 = somar(1, 7) # Passa dois valores: a = 1, b = 7, c = 0 → soma = 8
resposta_3 = somar(4) # Passa só um valor: a = 4, b = 0, c = 0 → soma = 4

print(f'Meus cálculos deram {resposta_1}, {resposta_2}, {resposta_3}.')

# -----------------------------------------------------------------------