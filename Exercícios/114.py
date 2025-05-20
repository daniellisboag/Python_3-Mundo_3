# Crie um código em python que teste se o site Pudim está acessível pelo computador usado.

from urllib import request, error

try:
   site = request.urlopen('https://pudim.com.br')
except error.URLError:
   print('O site Pudim não está acessível no momento.')
else:
   print('Consegui acessar o site Pudim com sucesso.')