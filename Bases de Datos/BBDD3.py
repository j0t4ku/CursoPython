#Ejemplo SQLITE3  Conceptos de UNIQUE

import sqlite3

Conexion= sqlite3.connect("Sqlite3Ejemplo3.sqlite3")

puntero=Conexion.cursor()

"""puntero.execute('''
    CREATE TABLE PRODUCTOS (
        cod_articulo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50) UNIQUE,
        precio INTEGER,
        seccion VARCHAR(20)
    )
''')"""

"""productos=[
    ("pelota",50000,"jugeteria"),
    ("pantalon",100000,"confeccion"),
    ("camisa",50000,"confeccion"),
]

puntero.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)
"""

#Listar Productos

"""puntero.execute("SELECT * FROM PRODUCTOS WHERE seccion='confeccion'")
listaP= puntero.fetchall()
print(listaP)
"""

#Actualizar UPDATE

"""puntero.execute("UPDATE PRODUCTOS SET precio=55000 WHERE cod_articulo=1")
"""

#Borrar DELETE

puntero.execute("DELETE FROM PRODUCTOS WHERE cod_articulo=3")



Conexion.commit()

Conexion.close()