from datetime import datetime

# Obtem a data e hora atuais
data_atual = datetime.now()

# Imprime o dia atual
print(data_atual.day)

# Imprime o mês atual
print(data_atual.month)

# Imprime o ano atual
print(data_atual.year)

# Imprime a hora atual
print(data_atual.hour)

# Imprime o minuto atual
print(data_atual.minute)

# Imprime o segundo atual
print(data_atual.second)

# Imprime a data e hora no formato 'd/m/Y H:M:S'
print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))