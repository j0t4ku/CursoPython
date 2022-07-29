from tkinter import *
from turtle import onclick
from webbrowser import get

##### Variables Globales ####

operacion=""
flag= ""
numeroSave =0


##### Raiz principal de la Interfaz
root= Tk()

#### Frame Principal de la Interfaz
frameP= Frame(root)
frameP.pack()

###### Pantalla ##########
numP= StringVar()
pantalla= Entry(frameP, textvariable=numP)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="white", justify="right")

##### Funcion de Pulsacion #####

def numPulsado(valor):
    global flag, operacion, numeroSave
    if flag != "":
        flag=""
        numeroSave= int(numP.get())
        numP.set(valor)
    else:
        numP.set(numP.get() + str(valor))

##### Funciones de Operaciones #####

def Operaciones(op):
    global operacion, numeroSave, flag
    flag= "holas" 
    if(operacion=="sum"):
        numeroSave = numeroSave +  int(numP.get())
        numP.set(str(numeroSave))
    elif(operacion=="res"):
        numeroSave = numeroSave -  int(numP.get())
        numP.set(str(numeroSave))
    elif(operacion=="mul"):
        numeroSave = numeroSave *  int(numP.get())
        numP.set(str(numeroSave))
    elif(operacion=="div"):
        numeroSave = numeroSave /  int(numP.get())
        numP.set(str(numeroSave))
    operacion= op

def resultado():
    global numeroSave, operacion
    Operaciones(operacion)
    numeroSave= 0
    operacion=""






######## Fila 1 ###########

boton7= Button(frameP, text="7", width=3, command=lambda:numPulsado("7"))
boton7.grid(row=2,column=1)
boton8= Button(frameP, text="8", width=3, command=lambda:numPulsado("8"))
boton8.grid(row=2,column=2)
boton9= Button(frameP, text="9", width=3, command=lambda:numPulsado("9"))
boton9.grid(row=2,column=3)
botonD= Button(frameP, text="/", width=3, command=lambda:Operaciones("div"))
botonD.grid(row=2,column=4)

######## Fila 2 ###########

boton4= Button(frameP, text="4", width=3, command=lambda:numPulsado("4"))
boton4.grid(row=3,column=1)
boton5= Button(frameP, text="5", width=3, command=lambda:numPulsado("5"))
boton5.grid(row=3,column=2)
boton6= Button(frameP, text="6", width=3, command=lambda:numPulsado("6"))
boton6.grid(row=3,column=3)
botonM= Button(frameP, text="X", width=3, command=lambda:Operaciones("mul"))
botonM.grid(row=3,column=4)

######## Fila 3 ###########

boton1= Button(frameP, text="1", width=3, command=lambda:numPulsado("1"))
boton1.grid(row=4,column=1)
boton2= Button(frameP, text="2", width=3, command=lambda:numPulsado("2"))
boton2.grid(row=4,column=2)
boton3= Button(frameP, text="3", width=3, command=lambda:numPulsado("3"))
boton3.grid(row=4,column=3)
botonR= Button(frameP, text="-", width=3, command=lambda:Operaciones("res"))
botonR.grid(row=4,column=4)


######## Fila 4 ###########

boton0= Button(frameP, text="0", width=3, command=lambda:numPulsado("0"))
boton0.grid(row=5,column=1)
botonD= Button(frameP, text=",", width=3, command=lambda:numPulsado(","))
botonD.grid(row=5,column=2)
botonI= Button(frameP, text="=", width=3, command=lambda:resultado())
botonI.grid(row=5,column=3)
botonS= Button(frameP, text="+", width=3, command=lambda:Operaciones("sum"))
botonS.grid(row=5,column=4)





root.mainloop()