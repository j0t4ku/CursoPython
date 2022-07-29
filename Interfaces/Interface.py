#Documentacion sobre tkinter 
#https://docs.python.org/3.9/library/tk.html

from tkinter import *

#Como el Frame principal de toda la interface
raiz= Tk()
raiz.title("Ventana Principal")
#Si la interfaz puede ser redimensionable
raiz.resizable(True,True)

#icono de la interfaz
raiz.iconbitmap("Icono.ico")

#Tamaño de la interfaz
raiz.geometry("720x600")

#backgraund fondo color
raiz.config(background="green")
raiz.mainloop()