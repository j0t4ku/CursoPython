#Ejercicio de Boton y 

from tkinter import *

root= Tk()
root.title("Ventana Principal")
root.iconbitmap("Icono.ico")
root.config(background="green")

FrameP= Frame(root, width=500, height=500)
FrameP.pack()

nombre= StringVar()

###  Cuadros de Texto ####
TextNombre= Entry(FrameP, textvariable=nombre)
TextNombre.grid(row= 0, column=1, padx=10, pady=10)
TextNombre.config(fg="black")

TextApellido= Entry(FrameP)
TextApellido.grid(row= 1, column=1, padx=10, pady=10)

TextDireccion= Entry(FrameP)
TextDireccion.grid(row= 2, column=1, padx=10, pady=10)

TextPass= Entry(FrameP)
TextPass.grid(row= 3, column=1, padx=10, pady=10)
TextPass.config(show="*")

#Cuadro de Texto De Comentarios 
TextCom= Text(FrameP, width=18, height=15)
TextCom.grid(row=4, column=1, padx=10, pady=10)


#Scroll
Scroll= Scrollbar(FrameP,command=TextCom.yview)
Scroll.grid(row=4, column=2, sticky="nsew")

TextCom.config(yscrollcommand=Scroll.set)




##### LABELS  #####
LabelNombre= Label(FrameP, text="Nombre: ")
LabelNombre.grid(row=0,column=0, sticky="w")

LabelApellido= Label(FrameP, text="Apellido: ")
LabelApellido.grid(row=1,column=0, sticky="w")

LabelDireccion= Label(FrameP, text="Direccion: ")
LabelDireccion.grid(row=2,column=0, sticky="w")

LabelPass= Label(FrameP, text="Contraseña: ")
LabelPass.grid(row=3,column=0, sticky="w")

LabelCom= Label(FrameP, text="Comentarios: ")
LabelCom.grid(row=4,column=0, sticky="w")


### Funcion BUTTON #####
def codigoBoton():
    nombre.set("Joel")


###  BUTTON #####
Boton1= Button(root, text="Enviar", command=codigoBoton)
Boton1.pack()



root.mainloop()