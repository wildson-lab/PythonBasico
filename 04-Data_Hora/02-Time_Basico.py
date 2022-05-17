# Criar Hora:
# Cria uma hora utilizando a biblioteca time e imprime a hora criada

from datetime import time

# Cria um novo horário
horario = time(hour=12, minute=15, second=28)

# Imprime o horário criado
print(horario.strftime('%H:%M:%S'))
