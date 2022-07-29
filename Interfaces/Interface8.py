# Dialogos de Fichero 
#Abrir un dialogo para abrir un archivo

from tkinter import * 
from tkinter import filedialog


root= Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Ficheros de Excel","*.xlsx"),("Ficheros de Texto","*.txt"),("Todos los Ficheros","*.*")))
    print(fichero)

Button(root, text="Abrir Fichero", command=abreFichero).pack()


root.mainloop()