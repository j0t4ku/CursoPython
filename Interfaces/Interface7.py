#Interfaces de Barra de Menus y Ventanas Emergentes(necesita ser importado)


from logging import info
from tkinter import *
from tkinter import messagebox
root=Tk()

#Defincion de funcion de ventana emergente

def infoAdicional():
    messagebox.showinfo("Procesador de joel","Procesador de texto 2022")

def avisoLicensia():
    messagebox.showwarning("Licencia","Licencia GNU")

def salir():
    #opcion=messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    opcion=messagebox.askyesno("Salir","¿Desea salir de la aplicacion?")
    if(opcion=="yes"):
        root.destroy()

def cerrarDocumento():
    opcion=messagebox.askretrycancel("Reintenta","¿Desea cerrar de la aplicacion?")    
    if(opcion==True):
        root.destroy()

barraMenu= Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu= Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=cerrarDocumento)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salir)

edicionMenu= Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


herramientaMenu= Menu(barraMenu, tearoff=0)


#Barra Ayuda
ayudaMenu= Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de", command=infoAdicional)
ayudaMenu.add_command(label="Licencia", command=avisoLicensia)

barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


root.mainloop()