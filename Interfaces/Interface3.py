#Ejercicio de Label
#Ejercicio Entry (TextBox)

from tkinter import *

root= Tk()
root.title("Ventana Principal")
root.iconbitmap("Icono.ico")
root.config(background="green")

FrameP= Frame(root, width=500, height=500)
FrameP.pack()
#Imagenes 
#Imagen1= PhotoImage(file="imagen1.png")
#Labelimg=Label(FrameP, image=Imagen1).place(x=25,y=150)

#Label Titulo en este caso
#Label1= Label(FrameP, text="Hola Mundo", font=("Arial",18),fg="red").place(x=150,y=0)

#Cuadro de Textos
TextNombre= Entry(FrameP)
TextNombre.grid(row= 0, column=1, padx=10, pady=10)
TextNombre.config(fg="black")

TextApellido= Entry(FrameP)
TextApellido.grid(row= 1, column=1, padx=10, pady=10)

TextDireccion= Entry(FrameP)
TextDireccion.grid(row= 2, column=1, padx=10, pady=10)

#Cuadro de Contraseña
TextPass= Entry(FrameP)
TextPass.grid(row= 3, column=1, padx=10, pady=10)
TextPass.config(show="*")



LabelNombre= Label(FrameP, text="Nombre: ")
LabelNombre.grid(row=0,column=0, sticky="w")

LabelApellido= Label(FrameP, text="Apellido: ")
LabelApellido.grid(row=1,column=0, sticky="w")

LabelDireccion= Label(FrameP, text="Direccion: ")
LabelDireccion.grid(row=2,column=0, sticky="w")

LabelPass= Label(FrameP, text="Contraseña: ")
LabelPass.grid(row=3,column=0, sticky="w")






root.mainloop()