#Interfaces con Radiobuttons  y Chebuttons

from tkinter import *

root=Tk()

opcion=IntVar()

#Funcion 
def imprimir():
    #print(opcion.get())
    if(opcion.get()==1):
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

#Radio butons
Label(root, text="Genero").pack()
Radiobutton(root,text="Masculino",variable=opcion, value=1, command=imprimir).pack()
Radiobutton(root,text="Femenino",variable=opcion, value=2, command=imprimir).pack()
etiqueta=Label(root)
etiqueta.pack()


#CheckButtons

playa=IntVar()
mont=IntVar()
city=IntVar()


def OpcionesViaje():
    text=""
    if(playa.get()==1):
        text+= " Playa"
    if(mont.get()==1):
        text+= " Montaña"
    if(city.get()==1):
        text+= " Ciudad"

    etiqueta2.config(text=text)

#Image
foto=PhotoImage(file="imagen1.png")
Label(root, image=foto).pack()


Label(root, text="CheckButtons").pack()
Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=OpcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=mont, onvalue=1, offvalue=0, command=OpcionesViaje).pack()
Checkbutton(root, text="Ciudad", variable=city, onvalue=1, offvalue=0, command=OpcionesViaje).pack()

etiqueta2=Label(root)
etiqueta2.pack()



root.mainloop()