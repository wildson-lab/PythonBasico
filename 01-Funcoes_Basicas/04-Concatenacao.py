# Concatenacao
# Este código mostra diferentes formas de concatenar variaveis em Python.

# Entrada de valores para as variaveis
nome = "Wildson"
idade = 26

# Imprime as informacoes presentes nas variaveis, concatenando com o texto
print("Olá, " + nome + "! Você tem " + str(idade) + " anos de idade.")

# Outra forma de concatenar:
print("Olá, {}! Você tem {} anos de idade.".format(nome, idade))

# Mais uma forma de concatenar:
print("Olá, {a}! Você tem {b} anos de idade.".format(a=nome,
                                                     b=idade))
