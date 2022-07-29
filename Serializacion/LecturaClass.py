import pickle
#Si la clase no esta en el mismo archivo de la deserializacion
#No funcionara ya que no sabe que es esa clase deserializada



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




fichero_A=open("losCoches","rb")
misCoches=pickle.load(fichero_A)
fichero_A.close()

for c in misCoches:
    c.estado()