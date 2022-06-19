# Adivinha numero
# Neste jogo, o jogador devera adivinhar um numero secreto aleatorio,
# Com o menor numero possivel de tentativas.

import random

print("Bem vindo ao jogo Adivinha Numero!")

n_dificuldade = 0
while not n_dificuldade in range(1, 6):
    n_dificuldade = int(input("Selecione um nivel de dificuldade entre 1 e 5: "))

n_max = (10 ** n_dificuldade) - 1

# numero_secreto = 324
numero_secreto = random.randint(1, n_max + 1)
acertou_numero = False
n_tentativas = 0

while not acertou_numero:
    chute = 0

    while not chute in range(1, n_max + 1):
        chute = int(input(f"Digite um numero entre 1 e {n_max}: "))

    n_tentativas += 1

    if chute < numero_secreto:
        print("Mais!")
    elif chute > numero_secreto:
        print("Menos!")
    else:
        print("Acertou!")
        print(f"Tentativas: {n_tentativas}")
        acertou_numero = True
