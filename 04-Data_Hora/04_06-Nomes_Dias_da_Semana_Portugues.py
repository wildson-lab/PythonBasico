# Nomes dos Dias da Semana (em Português):
# Obtém a data atual e o número que identifica o dia da semana, e
# imprime o nome do dia da semana correspondente em Português.
# OBS.: Em Python, a semana começa na segunda-feira.

from datetime import datetime

# Lista com os nomes em Português dos dias da semana
lista_dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo')

# Obtém a data e hora atuais
data_atual = datetime.now()

# Obtém o número correspondente ao dia da semana, sendo Segunda = 0 e Domingo = 6
dia_semana = data_atual.weekday()

# Imprime nome em Português do dia da semana atual
print('Hoje é {}.'.format(lista_dias[dia_semana]))