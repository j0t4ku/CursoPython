#Definicion de Clase en python
class Coche():

    def __init__(self):
        #encapsular la variable, protejer la variable de modificacion externa
        self.__largoChasis= 250
        self.__anchoChasis=120
        self.__ruedas= 4
        self.__enmarcha= False



    def arrancar(self, arrancar):
        self.__enmarcha= arrancar
        if(self.__enmarcha):
            chequeo= self.__check()
        
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo== False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"

    
    def estado(self):
        print("El coche tiene", self.__ruedas," rudas")
        print("El coche tiene", self.__largoChasis," de largo el chasis")
        print("El coche tiene", self.__anchoChasis," de ancho")

#Encapsular methodo, proteger el methodo de acceso externo
    def __check(self):
        print("Realizando Chequeos")
        self.gasolina="ok"
        self.aceite="ok"
        self.puerta="cerradas"
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
            return True
        else:
            return False
    





##Codigo
#Creamos el primer Objeto
print("\n### Creando primer objeto ###")  
miCoche= Coche()
print(miCoche.arrancar(True))
miCoche.estado()

#Creamos el segundo Objeto
print("\n### Creando segundo objeto ###")
miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
