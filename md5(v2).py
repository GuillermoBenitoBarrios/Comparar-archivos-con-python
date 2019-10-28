# Comparar si dos archivos son iguales mediante MD5 Checksum

# librerias
#import hashlib
import hashlib, sys

# paso de ficheros por argumento de shell
files = [sys.argv[1], sys.argv[2]] 
def md5(fname):
    md5hash = hashlib.md5()
    
    # Abriremos el fichero linea a linea, por cuestiones de memoria.
    with open(fname) as handle:
        for line in handle:
            md5hash.update(line.encode('utf-8'))
    return(md5hash.hexdigest())

def main():
    print('Comparando archivos',files[0],' y ',files[1], " usando MD5.")

    if md5(files[0]) == md5(files[1]):
        print('Coinciden.')
    else:
        print('No coinciden.')


if __name__ == "__main__":
    main()