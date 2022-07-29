#Polimorfismo 
#

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("Me dezplazo utilizando dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me dezplazo utilizando seis ruedas")


#Polimorfismo (El objeto vehiculo sabe que clase es)
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()



miVehiculo= Coche()
desplazamientoVehiculo(miVehiculo)