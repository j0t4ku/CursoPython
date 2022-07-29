#Ejemplo SQLITE3  Conceptos de Primary Key

import sqlite3

Conexion= sqlite3.connect("Sqlite3Ejemplo2.sqlite3")

puntero=Conexion.cursor()

puntero.execute('''
    CREATE TABLE PRODUCTOS (
        cod_articulo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(50),
        precio INTEGER,
        seccion VARCHAR(20)
    )
''')

productos=[
    ("pelota",50000,"jugeteria"),
    ("pantalon",100000,"confeccion"),
    ("camisa",50000,"confeccion"),
]

puntero.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

Conexion.commit()

Conexion.close()