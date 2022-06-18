# Este codigo demonstra a aplicacao de funcoes basicas de conjuntos em Python
# Conjunto e um tipo que não aceita repeticao de elementos.

# Cria um novo conjunto contendo numeros (um conjunto pode conter diversos tipos)
conjunto = {1, 2, 3, 4, 99, 5}

# Imprime o tipo "conjunto"
print(type(conjunto))

# Imprime os elementos de um conjunto
print(conjunto)

# Adiciona o numero 6 ao conjunto
conjunto.add(6)

# Remove o numero 99 do conjunto
conjunto.discard(99)

# Imprime o conjunto apos as alteracoes
print(conjunto)
