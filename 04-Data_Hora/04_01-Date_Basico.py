from datetime import date

# Obtém a data atual
data_atual = date.today()

# Imprime o dia atual
print(data_atual.day)

# Imprime o mês atual
print(data_atual.month)

# Imprime o ano atual
print(data_atual.year)

# Imprime a variável data_atual sem formatar
print(data_atual)

# Imprime a data atual no formato 'd/m/Y'
print(data_atual.strftime('%d/%m/%Y'))