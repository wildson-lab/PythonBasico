# 03 - Entrada e saida de dados
# Este codigo apresenta conceitos basicos sobre entrada de dados, e apresenta
# formas diversas de concatenar e imprimir informacoes no console.

# Entrada de valores para as variaveis
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Imprime as informacoes presentes nas variaveis, concatenando com o texto
print("Nome: " + nome)
print("Idade: " + str(idade))

# Outra forma de concatenar:
print("Nome: {}, idade: {} anos.".format(nome, idade))

# Mais outra forma de concatenar:
print("Nome: {a}, idade: {b} anos.".format(a=nome,
                                           b=idade))