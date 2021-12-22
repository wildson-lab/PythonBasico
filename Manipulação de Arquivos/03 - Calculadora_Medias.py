# Calculadora de Medias
# Neste exemplo, eh feita a leitura do arquivo 'notas.txt' com as notas de uma
# turma ficticia, e calculada a media para cada estudante. Cada linha do arquivo
# deve estar no seguinte formato: 'aluno,nota_1, nota_2, nota_3, nota_4'.
# Novas medias podem ser inseridas no arquivo pela funcao adicionar_notas.

import shutil

media = lambda notas: sum([float(i) for i in notas]) / 4

def calcula_medias(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    turma_notas = arquivo.read()
    aluno_notas = turma_notas.split('\n')
    lista_medias = []
    for x in aluno_notas:
        lista_notas = x.split(',')
        aluno_nome = lista_notas[0]
        lista_notas.pop(0)
        print(aluno_nome)
        print(lista_notas)
        aluno_media = media(lista_notas)
        lista_medias.append({aluno_nome: aluno_media})
    return lista_medias


def adicionar_aluno(nome_arquivo):
    nome_aluno = input('Digite o nome do aluno: ')
    nota_1 = float(input('Digite a primeira nota: '))
    nota_2 = float(input('Digite a segunda nota: '))
    nota_3 = float(input('Digite a terceira nota: '))
    nota_4 = float(input('Digite a quarta nota: '))
    arquivo = open(nome_arquivo, 'a')
    arquivo.write('\n{},{},{},{},{}'.format(nome_aluno, nota_1, nota_2, nota_3, nota_4))
    print('Notas salvas com sucesso!')
    arquivo.close()

if __name__ == '__main__':
    adicionar_aluno('notas.txt')
    medias = calcula_medias('notas.txt')
    print(medias)