import pickle
from tkinter import Misc


class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca)
        print("Modelo: ",self.modelo)
        print("En Marcha: ",self.enmarcha)
        print("Acelera: ",self.acelera)
        print("Frena: ",self.frena)

coche1=Vehiculos("Toyota","Allion")

coche2=Vehiculos("Mazda","MX5")

coche3=Vehiculos("Chevrolet","A10")


# Carga de Class
coches=[coche1,coche2,coche3]
fichero=open("losCoches","wb")
pickle.dump(coches,fichero)
fichero.close()
del(fichero)


#### Apertura del fichero


fichero_A=open("losCoches","rb")
misCoches=pickle.load(fichero_A)
fichero_A.close()

for c in misCoches:
    c.estado()

