# Este código mostra diferentes formas de concatenar variaveis em Python.

# Variaveis
nome = "Wildson"
idade = 26

# Diferentes formas para concatenar e formatar strings
string_1 = "Olá, " + nome + "! Você tem " + str(idade) + " anos de idade."
string_2 = "Olá, {}! Você tem {} anos de idade.".format(nome, idade)
string_3 = "Olá, {1}! Você tem {0} anos de idade.".format(idade, nome)
string_4 = "Olá, {a}! Você tem {b} anos de idade.".format(a=nome, b=idade)
string_5 = f"Olá, {nome}! Você tem {idade} anos de idade."

# Imprime o mesmo resultado
print(string_1)
print(string_2)
print(string_3)
print(string_4)
print(string_5)
