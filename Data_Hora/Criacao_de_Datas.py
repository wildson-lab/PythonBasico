# Criacao de Datas em Python

from datetime import datetime, timedelta

# Uma das formas para criar uma data
data_criada = datetime(2019, 6, 16, 14, 20, 00)

# Imprime o tipo da variável data_criada
print(type(data_criada))

# Imprime a data criada
print(data_criada.strftime('%d/%m/%Y %H:%M:%S'))

# Outra forma de criar uma data
outra_data = datetime.strptime('09/02/2018 12:20:00', '%d/%m/%Y %H:%M:%S')

# Imprime o tipo da variável outra_data
print(type(outra_data))

# Imprime a data criada
print(outra_data.strftime('%d/%m/%Y %H:%M:%S'))
