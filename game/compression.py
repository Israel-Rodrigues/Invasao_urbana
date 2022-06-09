import os
import zipfile
import sys

def getPath(file_or_folder):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, file_or_folder)
    return path

def zipdir(file_or_folder, ziph):
    path = getPath(file_or_folder)

    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def compression(file_or_folder):
    with zipfile.ZipFile(getPath(file_or_folder) + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(file_or_folder + '/', zipf)

def decompression(file_or_folder):
    with zipfile.ZipFile(getPath(file_or_folder), 'r', zipfile.ZIP_DEFLATED) as zipf:
        zipf.extractall('./')

def main():
    '''
    -------------------------------------------
    # Comando de compressão
    -------------------------------------------
    python ./compression.py -c ./images

    -------------------------------------------
    # Comando de descompressão
    -------------------------------------------
    python ./compression.py -d ./images.zip
    '''

    command = sys.argv[1] # Comando de compressão (-c) ou descompressão (-d)
    file_or_folder = sys.argv[2] # Caminho e arquivo que sera processado

    if command == '-c':
        compression(file_or_folder)
    elif command == '-d':
        decompression(file_or_folder)

    print('Process finished!')

if __name__ == "__main__":
    main()