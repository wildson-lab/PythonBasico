# Operacao com horas:
# Obtém a data e horas atuais, soma 3 horas, e imprime a nova data e hora.

from datetime import datetime, timedelta

# Obtem a data e hora atual
data_atual = datetime.now()

# Imprime a data e hota atuais no formato '%d/%m/%Y %H:%M:%S'
print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))

# Soma 3 horas
nova_data = data_atual + timedelta(hours=3)

# Imprime a nova data e hora no formato '%d/%m/%Y %H:%M:%S'
print(nova_data.strftime('%d/%m/%Y %H:%M:%S'))
