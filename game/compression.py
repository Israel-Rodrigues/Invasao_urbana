import os
import zipfile

target = 'projects\\invasao_urbana\\game\\images'
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, target)

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))

def images():
    with zipfile.ZipFile(path + '.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(target + '/', zipf)

    print('Compression finished')