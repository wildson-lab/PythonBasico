# Este arquivo  engloba as operacoes basicas para manipulacao de arquivos em
# Python em funcoes de uso mais simples.
# Pode ser usado como biblioteca.

# Abre um arquivo para escrita, criando novo arquivo ou reescrevendo um existente
def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close


# Abre um arquivo para escrita, permitindo adicionar mais conteudo
def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close


# Abre um arquivo para leitura, e imprime seu conteudo.
def imprimir_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    arquivo.close()
    print(texto)


# Abre um arquivo para leitura, e retorna seu conteudo.
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    arquivo.close()
    return texto


# Teste da biblioteca
if __name__ == '__main__':
    endereco_arquivo = 'teste.txt'
    escrever_arquivo(endereco_arquivo, 'Primeira linha.')
    atualizar_arquivo(endereco_arquivo, '\nSegunda linha.')
    imprimir_arquivo(endereco_arquivo)
    texto_arquivo = ler_arquivo(endereco_arquivo)
    print(texto_arquivo)
