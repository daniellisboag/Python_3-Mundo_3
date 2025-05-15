# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
# Adicione também as docstrings da função.

def notas(*notas, situacao = False):
   """
   -> Função para analisar notas e situações de vários alunos.
   :Parâmetro notas: Uma ou mais notas dos alunos (aceita várias).
   :Parâmetro situacao: Valor opcional, indicando se deve ou não adicionar a situação.
   :return: Dicionário com várias informações sobre a situação dos alunos.
   """
   dados = {'Total' : len(notas), 'Maior' : max(notas), 'Menor' : min(notas), 'Média' : sum(notas) / len(notas)}
   if situacao == True:
      if dados['Média'] >= 7:
         dados['Situação'] = 'Boa'
      elif dados['Média'] >= 5:
         dados['Situação'] = 'Razoável'
      else:
         dados['Situação'] = 'Ruim'
   return dados

resposta = notas(5.5, 2.5, 8.5, situacao = True)
print(resposta)
help(notas)