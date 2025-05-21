# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu
# nome e idade em um arquivo de texto simples. O sistema só vai ter 2 opções:
# cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from lib.interface import *
from lib.arquivo import *
from time import sleep

file = 'cursoemvideo.txt'

if not arquivo_existe(file):
   criar_arquivo(file)

while True:
   resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
   if resposta == 1:
      ler_arquivo(file)
   elif resposta == 2:
      cabeçalho('Novo cadastro')
      nome = input('Nome: ')
      idade = leia_int('Idade: ')
      cadastrar(file, nome, idade)
   elif resposta == 3:
      cabeçalho('Saindo do sistema! Até logo.')
      break
   else:
      print('\033[31mErro! Digite uma opção válida!\033[m')
   sleep(1)