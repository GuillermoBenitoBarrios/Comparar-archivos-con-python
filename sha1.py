# Comparar si dos archivos son iguales mediante SHA1

# librerias
#import hashlib
import hashlib, sys

# paso de ficheros por argumento de shell
files = [sys.argv[1], sys.argv[2]] 
def sha1(fname):
    sha1hash = hashlib.sha1()
    
    # Abriremos el fichero linea a linea, por cuestiones de memoria.
    with open(fname) as handle:
        for line in handle:
            sha1hash.update(line.encode('utf-8'))
    return(sha1hash.hexdigest())

def main():
    print('Comparando archivos',files[0],' y ',files[1], " usando SHA1.")

    if sha1(files[0]) == sha1(files[1]):
        print('Coinciden.')
    else:
        print('No coinciden.')


if __name__ == "__main__":
    main()