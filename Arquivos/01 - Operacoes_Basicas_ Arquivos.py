# Operacoes basicas com arquivos em Python
# Neste codigo mostra-se como abrir arquivos no modo de escrita 'w',
# adicao de conteudo 'a' e leitura 'r'.

# Abre o arquivo no modo de escrita (reescreve o arquivo) e adiciona uma linha
arquivo = open('teste.txt', 'w')
arquivo.write('Primeira linha do arquivo.\n')
arquivo.close

# Abre o arquivo para atualizacoes, adicionando mais uma linha no final.
arquivo = open('teste.txt', 'a')
arquivo.write('Segunda linha do arquivo.')
arquivo.close

# Abre o arquivo no modo leitura, e imprime o seu conteudo.
arquivo = open('teste.txt', 'r')
texto = arquivo.read()
print(texto)
