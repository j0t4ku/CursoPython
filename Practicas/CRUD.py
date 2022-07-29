#Ejercicio  de CRUD en Python


from tkinter import *
from tkinter import messagebox
import sqlite3



### Funciones

def conexiones():
    miconexion=sqlite3.connect("Usuarios.sqlite3")
    puntero= miconexion.cursor()
    try:
        puntero.execute('''
            CREATE TABLE DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR(50),
                PASS VARCHAR(50),
                APELLIDO VARCHAR(30),
                COMENTARIO VARCHAR(100)
            )
        ''')
        miconexion.commit()
        messagebox.showinfo("BBDD","Bases de Datos Creada Exitosamente")
    except:
        messagebox.showinfo("BBDD","Bases de Datos Ya Esta Creado")

#Funcion para salir de la aplicacion
def salirAplicacion():
    op= messagebox.askyesno("Salir","Desea salir de la aplicacion")
    if op:
        root.destroy()

#Funcion Limpiar campos
def limpiarCampos():
    ID.set("")
    Nombre.set("")
    Pass.set("")
    Apellido.set("")
    #Para borrar los Comentarios
    TextCom.delete(1.0, END)

#Funcion Crear
def crear():
    miconexion=sqlite3.connect("Usuarios.sqlite3")
    puntero= miconexion.cursor()
    datos=Nombre.get(),Pass.get(),Apellido.get(),TextCom.get("1.0",END)
    puntero.execute("INSERT INTO DATOSUSUARIOS VALUES(NULL,?,?,?,?)",(datos))
    miconexion.commit()
    messagebox.showinfo("Crear","Registro Insertado correctamentes")
    limpiarCampos()


#Funcion Leer
def leer():
    miconexion=sqlite3.connect("Usuarios.sqlite3")
    puntero= miconexion.cursor()
    puntero.execute("SELECT * FROM DATOSUSUARIOS WHERE ID="+ID.get()+"")
    elusuario= puntero.fetchall()
    for usuario in elusuario:
        ID.set(usuario[0])
        Nombre.set(usuario[1])
        Pass.set(usuario[2])
        Apellido.set(usuario[3])
        TextCom.insert(1.0, usuario[4])
    miconexion.commit()

#Funcion Actualizar
def acturalizar():
    miconexion=sqlite3.connect("Usuarios.sqlite3")
    puntero= miconexion.cursor()
    datos=Nombre.get(),Pass.get(),Apellido.get(),TextCom.get("1.0",END),ID.get()
    puntero.execute("UPDATE DATOSUSUARIOS SET NOMBRE=?, PASS=?, APELLIDO=?, COMENTARIO=? WHERE ID=?",(datos))
    miconexion.commit()
    messagebox.showinfo("Actualizar","Registro Actualizado correctamentes")
    limpiarCampos()

#Funcion Eliminar
def eliminar():
    miconexion=sqlite3.connect("Usuarios.sqlite3")
    puntero= miconexion.cursor()
    puntero.execute("DELETE FROM DATOSUSUARIOS WHERE ID="+ID.get())
    miconexion.commit()
    messagebox.showinfo("Eliminar","Registro Eliminado correctamentes")
    limpiarCampos()

# Interfaz Grafica
root= Tk()
barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#Conectar Menu
bbddMenu= Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexiones)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

#Borrar Campos
borrarMenu= Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Limpiar Campos", command=limpiarCampos)


#CRUD Menu
crudMenu= Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crear)
crudMenu.add_command(label="Leer", command=leer)
crudMenu.add_command(label="Actualizar", command=acturalizar)
crudMenu.add_command(label="Eliminar", command=eliminar)

#Ayuda Menu
ayudaMenu= Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de..")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#Frame de Campos de Texto
frame1= Frame(root)
frame1.pack()


#Para los Comentario no es necesario
ID=StringVar()
Nombre=StringVar()
Pass=StringVar()
Apellido=StringVar()

#Cuadros de Textos
Textid= Entry(frame1, textvariable=ID)
Textid.grid(row= 0, column=1, padx=10, pady=10)

TextNombre= Entry(frame1, textvariable=Nombre)
TextNombre.grid(row= 1, column=1, padx=10, pady=10)

TextPass= Entry(frame1, textvariable=Pass)
TextPass.grid(row= 2, column=1, padx=10, pady=10)
TextPass.config(show="*")

TextApellido= Entry(frame1, textvariable=Apellido)
TextApellido.grid(row= 3, column=1, padx=10, pady=10)

#Cuadro de Texto De Comentarios 
TextCom= Text(frame1, width=18, height=15)
TextCom.grid(row=4, column=1, padx=10, pady=10)

#Scroll
Scroll= Scrollbar(frame1,command=TextCom.yview)
Scroll.grid(row=4, column=2, sticky="nsew")
TextCom.config(yscrollcommand=Scroll.set)


#Label de Cuadros de Textos
LabelID= Label(frame1, text="ID: ")
LabelID.grid(row=0,column=0, sticky="e")

LabelNombre= Label(frame1, text="Nombre: ")
LabelNombre.grid(row=1,column=0, sticky="e")

LabelPass= Label(frame1, text="Pasword: ")
LabelPass.grid(row=2,column=0, sticky="e")

LabelApellido= Label(frame1, text="Apellido: ")
LabelApellido.grid(row=3,column=0, sticky="e")

LabelCom= Label(frame1, text="Comentarios: ")
LabelCom.grid(row=4,column=0, sticky="e")



#Frame Botones

frame2= Frame(root)
frame2.pack()

#Botones

btnCrear=Button(frame2, text="Crear", command=crear)
btnCrear.grid(row=0, column=0, sticky="e", padx=10, pady=5)


btnLeer=Button(frame2, text="Leer", command=leer)
btnLeer.grid(row=0, column=1, sticky="e", padx=10, pady=5)


btnActualizar=Button(frame2, text="Actualizar", command=acturalizar)
btnActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=5)


btnEliminar=Button(frame2, text="Eliminar", command=eliminar)
btnEliminar.grid(row=0, column=3, sticky="e", padx=10, pady=5)

root.mainloop()