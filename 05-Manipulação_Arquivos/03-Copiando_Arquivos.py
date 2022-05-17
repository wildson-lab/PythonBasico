import shutil

def copiar_arquivo(origem, destino):
    shutil.copy(origem, destino)

def mover_arquivo(origem, destino):
    shutil.move(origem, destino)

if __name__ == '__main__':
    copiar_arquivo('teste_copy.txt', 'C:/')
    mover_arquivo('teste_move.txt', 'C:/')
