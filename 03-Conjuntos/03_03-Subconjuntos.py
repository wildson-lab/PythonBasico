# 03 - Subconjuntos (Parte 2)
# Este codigo demonstra como verificar subconjuntos ou superconjuntos

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

# Verifica se A é subconjunto de B
conjunto_a_subset = conjunto_a.issubset(conjunto_b)
print("Conjunto A faz parte do Conjunto B: {}".format(conjunto_a_subset))

# Verifica se B é subconjunto de A
conjunto_b_subset = conjunto_b.issubset(conjunto_a)
print("Conjunto B faz parte do Conjunto A: {}".format(conjunto_b_subset))

# Verifica se A é superconjunto de B
conjunto_a_superset = conjunto_a.issuperset(conjunto_b)
print("Conjunto A engloba o Conjunto B: {}".format(conjunto_a_superset))

# Verifica se B é superconjunto de B
conjunto_b_superset = conjunto_b.issuperset(conjunto_a)
print("Conjunto B engloba o Conjunto A: {}".format(conjunto_b_superset))
