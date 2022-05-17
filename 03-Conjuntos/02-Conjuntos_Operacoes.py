# 02 - 03-Conjuntos (Parte 2)
# Este codigo demonstra a aplicacao de operacoes entre conjuntos

# Inicializa os conjuntos
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {4, 5, 6, 7, 8}

# Imprime ambos os conjuntos
print("Conjunto 1: {}".format(conjunto_1))
print("Conjunto 2: {}".format(conjunto_2))

# Uniao entre conjuntos:
conjunto_uniao = conjunto_1.union(conjunto_2)
print("Uniao entre os conjuntos: {}".format(conjunto_uniao))

# Intersecao entre conjuntos:
conjunto_intersecao = conjunto_1.intersection(conjunto_2)
print("Intersecao entre os conjuntos 1 e 2: {}".format(conjunto_intersecao))

# Diferenca do conjunto 1 para o conjunto 2
conjunto_diff_1 = conjunto_1.difference(conjunto_2)
print("Diferenca entre os conjuntos 1 e 2: {}".format(conjunto_diff_1))

# Diferenca do conjunto 2 para o conjunto 1
conjunto_diff_2 = conjunto_2.difference(conjunto_1)
print("Diferenca entre os conjuntos 2 e 1: {}".format(conjunto_diff_2))

# Diferenca simetrica entre os conjuntos
conjunto_diff_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print("Diferenca simetrica entre 1 e 2: {}".format(conjunto_diff_simetrica))
