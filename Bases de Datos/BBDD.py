#Ejemplo SQLITE3 

import sqlite3

Conexion= sqlite3.connect("Sqlite3Ejemplo.sqlite3")

puntero=Conexion.cursor()

#puntero.execute("CREATE TABLE PRODUCTOS (NOMBRE_A VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#Insertar uno a uno
#puntero.execute("INSERT INTO PRODUCTOS VALUES('BALON', 1500, 'DEPOERTE')")


## Insertar por tuplas 
#productos=[
#    ("camiseta",32000,"Deportes"),
#    ("Jarro",50000,"Ceramica"),
#    ("Camion",15000,"Jugueteria")
#]
#puntero.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",productos)

#es necesario para que la funcion se ejecute
##Conexion.commit()




##### Listar Poductos 
puntero.execute("SELECT * FROM PRODUCTOS")

listaProductos=puntero.fetchall()

for producto in listaProductos:
    print("Producto")
    print("Nombre producto: ",producto[0])
    print("Precio producto: ",producto[1])
    print("Categoria producto: ",producto[2])


Conexion.close()