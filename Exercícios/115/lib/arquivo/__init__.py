from lib.interface import cabeçalho

def arquivo_existe(nome):
   try:
      file = open(nome, 'rt')
      file.close()
   except FileNotFoundError:
      return False
   else:
      return True

def criar_arquivo(nome):
   try:
      file = open(nome, 'wt+')
      file.close()
   except:
      print('Houve um erro na criação do arquivo!')
   else:
      print(f'Arquivo {nome} criado com sucesso!')

def ler_arquivo(nome):
   try:
      file = open(nome, 'rt')
   except:
      print('Erro ao ler o arquivo!')
   else:
      cabeçalho('Pessoas cadastradas')
      for c in file:
         dado = c.split(';')
         dado[1] = dado[1].replace('\n', '')
         print(f'{dado[0]:<30}{dado[1]:>7} anos')
   finally:
      file.close()

def cadastrar(arquivo, nome = 'Desconhecido', idade = 0):
   try:
      file = open(arquivo, 'at')
   except:
      print('Houve um erro na abertura do arquivo!')
   else:
      try:
         file.write(f'{nome}; {idade}\n')
      except:
         print('Houve um erro na hora de registrar os dados!')
      else:
         print(f'Novo registro de {nome} adicionado com sucesso.')
         file.close()