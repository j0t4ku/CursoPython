from tkinter import *
from turtle import right

raiz= Tk()

raiz.title("Ventana Principal")

raiz.iconbitmap("Icono.ico")

#raiz.geometry("720x600")

raiz.config(background="green")
raiz.config(bd=24)
raiz.config(relief="groove")

Frame1= Frame()

#Asia donde se ancla el frame (side="left", anchor="n")
#Expansion o redimension del frame fill="y", expand="True" con x no es necesario expand
##con both se expande con la raiz

#Frame1.pack(fill="both", expand="True")


Frame1.pack()
Frame1.config(background="red")
Frame1.config(width="200", height="200")

#borde bd=24 tipo de borde relief="groove"
Frame1.config(bd=24)
Frame1.config(relief="groove")

Frame1.config(cursor="hand2")


#loop infinito para
raiz.mainloop()