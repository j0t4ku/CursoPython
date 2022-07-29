#Herencia
#Herencia Simple y Multiple (Python si lo acepta)

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


class Furgoneta(Vehiculos):
    capacidad= False
    def carga(self, carga):
        self.capacidad= carga
        if(self.capacidad):
            return "La furgoneta esta cargado"
        else:
            return "La  furgoneta no esta cargado"


class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Haciendo caballito"
    #Invalida el estado de la clase padre (sobreescritura de metodos)
    def estado(self):
        print("Marca: ",self.marca)
        print("Modelo: ",self.modelo)
        print("En Marcha: ",self.enmarcha)
        print("Acelera: ",self.acelera)
        print("Frena: ",self.frena)
        print("Caballito: ",self.hcaballito)


class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia= 100
    
    def cargarEnergia(self):
        self.cargando=True


#Da prioridad a la primera clase definida 
class BicicletaElectrica(VElectricos, Vehiculos):
    pass




miMoto= Moto("Kawasaki", "M150")
miMoto.caballito()
miMoto.estado()

print("Creando Furgoneta")
miFurgoneta= Furgoneta("Hyndai", "EA150")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

print("Creando Bici")

#
miBici= BicicletaElectrica("Orbeo","J5")
