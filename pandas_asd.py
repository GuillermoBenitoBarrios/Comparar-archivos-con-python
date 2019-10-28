# Comparar si dos archivos son iguales mediante eq() de la libreria pandas

#pip install pandas
# Cargar las librerias
#import pandas as pd

# Leer archivo
#archivo_ejemplo_bbd_clientes1 = pd.read_csv('Ejemplo_BDD_Clientes.csv', quotechar ='"',sep =';', encoding ='utf8')
# mostramos las 5 primeras entradas del archivo
#archivo_ejemplo_bbd_clientes1.head(5)

# Leemos la copia del archivo anterior
#archivo_ejemplo_bbd_clientes2 = pd.read_csv('Ejemplo_BDD_Clientes - copia.csv', quotechar ='"',sep =';', encoding ='utf8')
# mostramos las 5 primeras entradas del archivo
#archivo_ejemplo_bbd_clientes2.head(5)

# leer archivos por argumentos de shell
import sys, sqlite3
import pandas as pd
archivos = [sys.argv[1], sys.argv[2]] #these are the arguments we take
#archivo_ejemplo_bbd_clientes1 = pd.read_csv(archivos[0])
#archivo_ejemplo_bbd_clientes2 = pd.read_csv(archivos[1])
archivo_ejemplo_bbd_clientes1 = pd.read_csv(archivos[0], quotechar ='"',sep =';', encoding ='utf8')
archivo_ejemplo_bbd_clientes2 = pd.read_csv(archivos[1], quotechar ='"',sep =';', encoding ='utf8')


print("\nComparación utilizando pandas - método Eq():\n")


# Eq()
# Comparando usando el metodo eq() de la libreria pandas
comparacion = archivo_ejemplo_bbd_clientes1.eq(archivo_ejemplo_bbd_clientes2)
#comparacion

# podemos imprimir el resultado final de la comparación con print tambien:
print(comparacion)

# Utilizamos el metodo all() para comprobar si los valores de toda una columna son True o existe alguna discrepancia, en cuyo caso será False.
#comparacion.all()
#print(comparacion.all())

# Repetimos la operación, pero en este caso realizaremos una comparación por filas 
comparacion_por_filas = comparacion.all(axis=1)
#comparacion_por_filas

#Podemos convertir los resultados obtenidos en un dataframe, y filtrar los valores, para averiguar cuales tienen un valor False.
comparacion_por_filas = pd.DataFrame(comparacion_por_filas, columns=['Columnas'])
#comparacion_por_filas[comparacion_por_filas['Columnas']==False]
print(comparacion_por_filas[comparacion_por_filas['Columnas']==False])



# equals()
#df3 = archivo_ejemplo_bbd_clientes1.equals(archivo_ejemplo_bbd_clientes2)
#print('Matches:', df3)
print("\nComparación utilizando pandas - método equals():\n")

comparacion_equals = archivo_ejemplo_bbd_clientes1.equals(archivo_ejemplo_bbd_clientes2)
comparacion_equals
print('Iguales:', comparacion_equals)


# any()
print("\nComparación utilizando pandas - método any():\n")

# comparación completa entre dos archivos.
comparacion_any = (archivo_ejemplo_bbd_clientes1 != archivo_ejemplo_bbd_clientes2).any(axis=None)
print('¿Diferencias entre los dos archivos?:', comparacion_any)

# Si hay diferencias, las muestra
if (comparacion_any):
    # El método .stack() nos permite apilar los datos. Se utiliza para remodelar el aspecto que tienen los datos
    diferencias_stacked = (archivo_ejemplo_bbd_clientes1 != archivo_ejemplo_bbd_clientes2).stack()


    # Filtramos los valores que sean True:
    diferencias = diferencias_stacked[diferencias_stacked]
    diferencias

    # etiquetamos los valores de las columnas:
    diferencias.index.names = ['id', 'columna']
    #diferencias

    print('Diferencias en:')
    print(diferencias)