# Dentro do pacote UtilidadesCeV que criamos no desafio 111, temos um módulo chamado dado.
# Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(),
# mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from UtilidadesCeV import Dado, Moeda

valor = Dado.leiaDinheiro('Digite um valor: R$')
Moeda.resumo(valor, 35, 22)